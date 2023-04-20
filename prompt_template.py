import streamlit as st
import pandas as pd

#language
lan = st.sidebar.selectbox(
    " ",
    ("EN", "VN")
)

if lan == "EN":
    S1 = '### Situation and quesion'
    S2 = "Your detail situation:"
    S3 = "Your question:"
    S4 = '### Helper'
    S5 = '### Your nearly perfect prompt is:'
    csv_path = 'EN.csv'

if lan == "VN":
    S1 = '### Tình huống và câu hỏi'
    S2 = "Chi tiết về tình huống của bạn:"
    S3 = "Câu hỏi của bạn:"
    S4 = '### Trợ giúp'
    S5 = '### Câu prompt gần hoàn hảo của bạn:'
    csv_path = 'VN.csv'


# Set the path of the CSV file

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_path)

# Print the DataFrame to verify that it was read correctly
# print(df['Prompt'])

#general inputs
st.write(S1)
mySituation = st.text_input(S2)
myQuestion = st.text_input(S3)

st.write(S4)
#side bar Helper
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

st.write(S5)

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
