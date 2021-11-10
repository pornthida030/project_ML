from ast import dump
from flask import Flask,render_template,request
from flask.helpers import url_for
from werkzeug.utils import redirect
import models 

app=Flask(__name__)

@app.route('/')
def index():
    get_type=models.getType()
    return render_template("index.html",type_se=get_type)

@app.route('/warn')
def warn():
    month=request.args.get('type_month')
    if(month=="1"):
        month_text="มกราคม"
    elif(month=="2"):
        month_text="กุมภาพันธ์"
    elif(month=="3"):
        month_text="มีนาคม"
    elif(month=="4"):
        month_text="เมษายน"
    elif(month=="5"):
        month_text="พฤษภาคม"
    elif(month=="6"):
        month_text="มิถุนายน"
    elif(month=="7"):
        month_text="กรกฎาคม"
    elif(month=="8"):
        month_text="สิงหาคม"
    elif(month=="9"):
        month_text="กันยายน"
    elif(month=="10"):
        month_text="ตุลาคม"
    elif(month=="11"):
        month_text="พฤศจิกายน"
    elif(month=="12"):
        month_text="ธันวาคม"
    else:
        month_text="ไม่ปรากฏ"
    price=request.args.get('price')
    pro=request.args.get('type_pro')
        
    pre,sco=models.perdict_price(pro,int(month),float(price))
    print(pre)
    if(pre[0]==1):
        predic="ไม่น่าซื้อ"
    elif(pre[0]==0):
        predic="น่าซื้อ"
    else:
        predic="ไม่สามารถทำนายได้"
    avg=models.getavg(pro,int(month))
    return render_template("warn.html",month_text=month_text,price=price,pro=pro,text_predict=predic,predict=pre,score=sco,avg=avg)
    
    

if __name__ =="__main__":
    app.run(debug=True)