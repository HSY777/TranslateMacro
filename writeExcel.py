df = pd.DataFrame({'startSentence': startWord, 'arriveSentence': list_arriveWord})
df.to_excel('input_sentence.xlsx', sheet_name='new_name', index=False, header=True)
progress_label.config(text = '완료')