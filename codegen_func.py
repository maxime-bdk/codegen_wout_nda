from pprint import pprint
from ndaclient import AsyncNDAClient, NDAClient
import re

def main():
    with NDAClient('NDA', 'NDA', 'NDA') as nda_client:
        alg_name = "The algorithm name from the ui"
        llm_answer = "the llm answer from the ui"
        # Randomly generated
        alg_id = None
        alg_ident = "alg ident from the ui"
        # Extract the code block with regex (before removing newlines)
        pattern = r'```(?:groovy)?\n([\s\S]*?)```'
        matches = re.findall(pattern, llm_answer)

        result = {}

        if matches:
            # Join multiple matches with double newlines
            llm_answer = '\n\n'.join(match.strip() for match in matches)

        result = {}

        try: 
            if alg_id is None:
                # Create new algorithm
                alg_id = nda_client.create_alg(
                    name=alg_name, 
                    ident=alg_ident, 
                    base_type_id=None, 
                    code=llm_answer
                )
            else:
                # update current algorithm
                nda_client.update_object(alg_id, values={'COMPILED_CODE': llm_answer})
                print(answer)

            answer = nda_client.eval_alg(alg_id)
            result['alg_id'] = alg_id
            result['alg_msg'] = answer
            result['clean_llm_answer'] = llm_answer
            return result

        except Exception as e:
        # Catch compilation/execution errors
            result['alg_id'] = alg_id
            result['alg_msg'] = str(e)
            result['clean_llm_answer'] = llm_answer
            return result


main()