import os
import json 

def main(convos_folder):
    convos = []
    # dictionary of messages 
    
    # look through each file in the the convos_folder path and check if it is a .txt document
    for filename in os.listdir(convos_folder):
        
        if filename.endswith(".txt"):

            filepath = os.path.join(convos_folder, filename)

            with open(filepath, 'r') as f:
                msgs = []   
                for line in f:
                    if line.strip() == '':
                        continue
                    print(line)
                    user, prompt = line.split(':', 1)
                    user = user.strip()
                    prompt = prompt.strip()

                    msgs.append({
                        'role': user,
                        'content': prompt
                    })
                convos.append(msgs)
                

    

    # save messages to a json file
    with open('messages.json', 'w') as f:
        for convo in convos:
            json.dump({ 'messages': convo}, f)
            f.write('\n')


if __name__ == '__main__':
    
    convos_folder = r"C:\Users\willi\Downloads\finetuning-main\finetuning-main\convos"
    messages = main(convos_folder) 

    # for message in messages: 
    #     print(message)