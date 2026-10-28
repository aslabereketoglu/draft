"""Session-only interface for the teammates' Tool 1 judge."""
from dataclasses import asdict
import json
import streamlit as st
from app.tool1.rubrics import RUBRICS


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
            try:
                from app.tool1.config import load_settings
                from app.tool1.judge import judge
                try:
                    load_settings()
                except RuntimeError:
                    st.error('GW Azure settings are missing. Configure the required settings in your local .env file; never paste API keys into chat or commit them to GitHub.')
                else:
                    with st.spinner('Reviewing the draft…'):
                        result=judge(draft,kind)
                    st.session_state['tool1_result']={'draft':draft,'result':asdict(result)}
            except ImportError:
                st.error('Install requirements-tool1.txt to enable the model connection.')
            except Exception:
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
        for name,rating in result['dimensions'].items():
            st.write('**'+name.replace('_',' ')+'**')
            st.write(f'Status: {rating["status"]}; score: {rating["score"] if rating["score"] is not None else "Not scored"}')
            for quote in rating['evidence']:
                st.text('Evidence: '+quote)
            st.write(rating['note'])
        for warning in result['warnings']:
            st.warning(warning)
        st.download_button('Download Message Review',json.dumps(saved,indent=2),file_name='commsalign-message-review.json',mime='application/json')
        st.button('Clear message and result',on_click=clear_message)
