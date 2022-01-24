import json
student={"name":"ivan","height":184,"citizen_Ukraine":True}
file=open("student.json","w")
json.dump(student,file,ensure_ascii=False)
file.close()
    