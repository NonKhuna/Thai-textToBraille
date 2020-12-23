# Thai-textToBraille
ระบบแปลง text ภาษาไทยเป็น braille ปัจุบันมี 2 รูปแบบคือ
* ลักษณะการอ่าน เช่น "1234"(อ่าน จุด 1 จุด 2 จุด 3 จุด 4) แทน "ก"
* ลักษณะ braille comp code เช่น "G"  แทน "ก" <b>


## Video
รายละเอียดเพิ่มเติม [Fullpaper](https://drive.google.com/file/d/1iigT8oj_bSI5u6O4JsVlRwSub1pmlDol/view?usp=sharing)


## Requirment
- pythainlp library

## Setup Environment
```shell
$ pip install -r requirements.txt
```

## How to use
```shell
$ python app.py -t <ข้อความที่ต้องการแปลง> -p <path ไฟล์ .txt> -m <mode>
```
* `-t` นำเข้าข้อมูล text
* `-p` นำเข้า path ไฟล .txt เพื่อแปลงทั้งไฟล์
* `-m` mode ที่ใช้ในการแปลง โดย 
  * `0` T2SB ลักษณะการอ่าน เช่น 124|1245|3|1236|(เก็บ) เป็นต้น
  * `1` T2BC braille comp code เช่น gra!%(กระเซอ)


## Reference
* [คู่มืออักษรเบรลล์](https://drive.google.com/drive/folders/1Q94Doe6sNTrUHup1C3LJ5LcGxhdIS1mj?usp=sharing)
