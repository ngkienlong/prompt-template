import streamlit as st
import pandas as pd


# Set the path of the CSV file
csv_path = 'prompts.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_path)

# Print the DataFrame to verify that it was read correctly
# print(df['Prompt'])

#general inputs
st.write('### Describe your situation and your quesion:')
mySituation = st.text_input("Your detail situation:")
myQuestion = st.text_input("Your question:")

st.write('### For better prompt:')
#side bar
prompts = []
for j in range(len(df)):
    if df['Default'][j] == 0:
        prompts.append(st.sidebar.checkbox(df['Prompt'][j]))
    else:
        prompts.append(st.sidebar.checkbox(df['Prompt'][j],value=True))
# templates = st.sidebar.selectbox('Templates:',df['Prompt'])

#detail input
inputs = {}
for i in range(len(df)):
    if (df['Need input'][i] == 1) & prompts[i]:
        inputs[df['Prompt'][i]] = st.text_input(df['Full text'][i])


final_prompt = ""
# final_prompt += myQuestion + '? '

# for input in inputs:
#     final_prompt += input
#     final_prompt += inputs[input]

st.write('### Your nearly perfect prompt is:')

for i in range(len(df)):
    if prompts[i] & (df['Before detail'][i] == 1):
        if df['Need input'][i] == 1:
            final_prompt += df["Full text"][i] + ' '
            if inputs[df["Prompt"][i]] == "":
                if df['Quote'][i] == 1:
                    final_prompt += '"..." '
                else:
                    final_prompt += "..."
            else:
                if df['Quote'][i] == 1:
                    final_prompt += '"' + inputs[df["Prompt"][i]] + '"' + '. '
                else:
                    final_prompt += inputs[df["Prompt"][i]] + '. '
        else:
            final_prompt += df["Full text"][i] + '. '

if mySituation != "":
    final_prompt += mySituation + ". "
if myQuestion != "":
    final_prompt += 'My question for you is : '+myQuestion + "? "

for i in range(len(df)):
    if prompts[i] & (df['Before detail'][i] == 0):
        if df['Need input'][i] == 1:
            final_prompt += df["Full text"][i] + ' '
            if inputs[df["Prompt"][i]] == "":
                if df['Quote'][i] == 1:
                    final_prompt += '"..." '
                else:
                    final_prompt += "..."
            else:
                if df['Quote'][i] == 1:
                    final_prompt += '"' + inputs[df["Prompt"][i]] + '"' + '. '
                else:
                    final_prompt += inputs[df["Prompt"][i]] + '. '
        else:
            final_prompt += df["Full text"][i] + '. '

st.write(final_prompt)
