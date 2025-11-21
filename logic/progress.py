import json, os
DATA=os.path.join(os.path.dirname(os.path.dirname(__file__)),'data','progress.json')
def load_progress():
    try:
        with open(DATA,'r') as f: return json.load(f)
    except: return {'sessions':[]}
def save_progress_entry(name,shape,d1,d2,student_ans,correct_area,ok):
    data=load_progress()
    entry={'name':name or 'Student','shape':shape,'dimensions':{'d1':d1,'d2':d2},'student_answer':student_ans,'correct_answer':correct_area,'result':'correct' if ok else 'incorrect'}
    data.setdefault('sessions',[]).append(entry)
    with open(DATA,'w') as f: json.dump(data,f,indent=2)
