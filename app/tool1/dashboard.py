"""Session-only interface for the teammates' Tool 1 judge."""
from dataclasses import asdict
import json
import re
import streamlit as st
import altair as alt
from app.tool1.rubrics import RUBRICS


def dimension_label(name):
    return re.sub(r'^[DF]\d+_', '', name).replace('_',' ').capitalize()


def score_chart(result):
    if result['abstain']:
        return
    rows=[]
    unscored=[]
    for name,rating in result['dimensions'].items():
        label=dimension_label(name)
        if rating['status']=='scored' and rating['score'] is not None:
            rows.append({'Dimension':label,'Score':rating['score'],'Baseline':1})
        else:
            unscored.append(label)
    if rows:
        st.subheader('Rubric scores')
        chart=alt.Chart(alt.Data(values=rows)).encode(
            y=alt.Y('Dimension:N',sort=[row['Dimension'] for row in rows],title=None),
            x=alt.X('Score:Q',scale=alt.Scale(domain=[1,5],zero=False),
                    axis=alt.Axis(values=[1,2,3,4,5]),title='Score (1–5)'),
            tooltip=['Dimension:N','Score:Q'],
        )
        bars=chart.mark_bar(color='#2F75B5',size=22).encode(x2='Baseline:Q')
        points=chart.mark_point(filled=True,color='#2F75B5',size=65)
        labels=chart.mark_text(align='left',dx=9,color='#20334A').encode(text='Score:Q')
        st.altair_chart((bars+points+labels).properties(height=max(120,len(rows)*48)),use_container_width=True)
        st.caption('Bars start at 1, the lowest rubric score. Higher scores indicate closer alignment with the rubric.')
    if unscored:
        st.caption('Not scored: '+', '.join(unscored)+'. See the explanations below.')


def clear_message():
    st.session_state['tool1_result']=None
    st.session_state['tool1_draft']=''


def main():
    st.set_page_config(page_title='CommsAlign — Message Coach',layout='wide')
    st.title('Tool 1 — Message Coach')
    st.write('Review a task instruction or performance feedback draft using the team’s rubric.')
    st.info('Scores are rubric-based model judgments, not validated measures of communication effectiveness. Review the evidence and output yourself.')
    st.caption('Evaluation sends your draft to the configured GW Azure service only when you submit it with consent. No message is sent to employees. The rewriter/RAG component is not implemented. Avoid identifying or sensitive content.')
    st.session_state.setdefault('tool1_result',None)
    if (st.session_state['tool1_result'] or {}).get('sample'):
        st.session_state['tool1_result']=None
    with st.form('tool1_review'):
        kind=st.selectbox('Message type',list(RUBRICS),format_func=lambda value:value.replace('_',' ').title())
        draft=st.text_area('Draft message',height=200,key='tool1_draft')
        consent=st.checkbox('I agree to send this draft to the configured GW Azure model for evaluation.')
        submit=st.form_submit_button('Evaluate draft')
    if submit:
        st.session_state['tool1_result']=None
        if not draft.strip():
            st.error('Enter a draft message to evaluate.')
        elif not consent:
            st.error('Confirm the model submission before evaluating.')
        else:
            progress=st.progress(10,text='10% — Checking connection settings')
            st.caption('Progress reflects review stages. It stays at 25% while the model responds.')
            try:
                from app.tool1.config import load_settings
                from app.tool1.judge import judge
                try:
                    load_settings()
                except RuntimeError:
                    progress.empty()
                    st.error('GW Azure settings are missing. Configure the required settings in your local .env file; never paste API keys into chat or commit them to GitHub.')
                else:
                    progress.progress(25,text='25% — Reviewing your draft against the rubric…')
                    with st.spinner('Reviewing the draft…'):
                        result=judge(draft,kind)
                    st.session_state['tool1_result']={'draft':draft,'result':asdict(result)}
                    progress.progress(100,text='100% — Review complete. Your results are below.')
            except ImportError:
                progress.empty()
                st.error('Install requirements-tool1.txt to enable the model connection.')
            except Exception:
                progress.empty()
                st.error('Evaluation could not be completed. Check the GW connection settings and model access, then retry. No result has been substituted.')
    with st.expander('Connection setup and rubric'):
        st.write('Install requirements-tool1.txt, then copy .env.example to .env and enter your GW-provided settings locally. Never commit .env.')
        st.code('GW_AZURE_OPENAI_KEY\nGW_ENDPOINT\nGW_API_VERSION\nGW_MODEL')
        st.markdown(RUBRICS[kind].text())
    saved=st.session_state['tool1_result']
    if saved:
        result=saved['result']
        st.subheader('Evaluation of the last submitted draft')
        st.text(saved['draft'])
        if result['abstain']:
            st.warning('Judge abstained: '+str(result['abstain_reason'] or 'Outside rubric scope.'))
        else:
            st.write('Rubric label: '+str(result['label']).replace('_',' '))
        st.caption('Model-reported confidence: '+result['confidence_level']+' — '+result['confidence_note'])
        score_chart(result)
        for name,rating in result['dimensions'].items():
            st.write('**'+dimension_label(name)+'**')
            st.write(f'Status: {rating["status"]}; score: {rating["score"] if rating["score"] is not None else "Not scored"}')
            for quote in rating['evidence']:
                st.text('Evidence: '+quote)
            st.write(rating['note'])
        for warning in result['warnings']:
            st.warning(warning)
        st.download_button('Download Message Review',json.dumps(saved,indent=2),file_name='commsalign-message-review.json',mime='application/json')
        st.button('Clear message and result',on_click=clear_message)
