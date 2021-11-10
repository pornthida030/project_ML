### ชื่อ พรธิดา สุขสรรควณิช รหัสนิสิต 6210451314 หมู่ 200
### Web 
- Framework ที่ใช้ [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- Frontend Framework ที่ใช้ Bootstrap

### Model
- ใช้ K-nearest neighbors algorithm ในการทำนาย

### วิธีใช้
1. จะต้องติดตั้ง Python 3.7.x และ Flask มาก่อน
2. ไปที่ app.py กดรัน และรอสักพัก จะขึ้น url ให้กดเข้า url นั้น
3. เลือกสินค้า เดือน ราคาตามที่ต้องการ กดทำนาย จะแสดงผลลัพธ์ออกมาว่าน่าซื้อหรือ (ในการเลือกสินค้าจะเป็นสินค้าที่มีใน Data set เท่านั้น)

### ไฟล์
- noit11561118811.csv เป็นไฟล์ของ Data set
- app.py เอาไว้รัน
- models.py เป็นตัวโมเดลที่ใช้งานจริงกับ หน้าเว็บ
- checkModel.ipynb เป็นโมเดลรูปแบบ jupyter notebook
- model.pdf เป็นโค้ดโมเดลแบบ jupyter notebook ซึ่งมาจาก checkModel.ipynb
- Predict_Agricultural_Price_Present.pdf เป็นสไลด์ที่จัดทำ