import streamlit as st
from PIL import Image
from io import BytesIO
import base64
from ultralytics import YOLO
import os
from statistics import mean, mode
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import numpy as np



#โหลด yolo model 
@st.cache_resource
def load_model(path):
    return YOLO(path)

#function ใช้ show รายละเอียดดอกไม้แต่ละชนิด
def show_information(name):
    # check ว่า predict ได้คลาสไหน แล้วเอาข้อมูลคลาสนั้นมาแสดง
    if  name=="Orchidaceae_Smitinandia":
        st.info('''
    **กล้วยไม้เข็มหนู/กุหลาบดง**
        
    **ชื่อวิทยาศาสตร์** : Smitinandiamicrantha
        
    **สกุล** : เข็ม (Ascocentrum)
        
    **ลักษณะทางพฤกษศาสตร์** : เป็นกล้วยไม้ที่มีใบเป็นแบบใบกลม มีร่องลึกทางด้านบนของใบ 
    ใบกว้างประมาณ 5 มิลลิเมตร มีดอกสีม่วงอ่อนช่อดอกตั้งหรือเอนเล็กน้อย ยาวใกล้เคียงใบ 
    ดอกในช่อโปร่ง ขนาดดอก 0.6-1เซนติเมตร   

    **วิธีการปลูก** : ปลูกในกระถาง ติดแผ่นไม้ วัสดุปลูกที่ใช้เช่น กาบมะพร้าวสับ 
    หากปลูกติดกิ่งหรือลำต้นควรเลือกต้น ที่มีเปลือกที่สามารถดูดซับความชื้นได้ดี
    ทรงพุ่มไม่หนาทึบ อากาศถ่ายเทสะดวก    

    **การรดนํ้า** : รดน้ำสม่ำเสมอ ปริมาณน้ำที่พอดีไม่มากและไม่น้อยจนเกินไป 

    **แสงแดด** : แดดรำไร 

    **ขยายพันธุ์** : ขยายพันธ์ุโดยการแบ่งกอ หรือเพาะเมล็ด ''')

    elif name=="Orchidaceae_DendrobiumFormosum":
        st.info('''
    **กล้วยไม้เอื้องเงินหลวง/เอื้องตาเหิน**
        
    **ชื่อวิทยาศาสตร์** : Dendrobium formosum 

    **สกุล** : หวาย (Dendrobium) 

    **ลักษณะทางพฤกษศาสตร์** : เป็นกล้วยไม้อิงอาศัย สูง 25-50 ซม. ลำต้นรูปแท่งดินสอกลม 
    โคนเรียวและคอด ก้านใบมีขนสีดำ ใบเป็นรูปรีแกมรูปขอบขนาน  กว้างประมาณ 2-2.5 ซม. 
    ยาว 6-8 ซม. ออกเรียงสลับตามข้อลำต้น ปลายและโคนใบแหลม สีเขียวสดเป็นมันและมักจะทิ้งใบเวลาผลิดอก   

    **วิธีการปลูก** : ใช้วัสดุที่เก็บความชื้นได้ดี โปร่ง ระบายน้ำและอากาศดี เช่น ถ่านทุบ 
    อิฐมอญทุบ กาบมะพร้าว รากเฟินชายผ้าสีดา เศษกระถางแตก หินภูเขาไฟ เป็นต้น 

    **การรดนํ้า** : รดน้ำปานกลาง ไม่มากและน้อยจนเกินไป 

    **แสงแดด** : แดดรำไร หรือได้รับแสงในช่วงเช้า 

    **ขยายพันธุ์** : ขยายพันธุ์โดยการแยกกอหรือเพาะเลี้ยงเนื้อเยื่อ''')

    elif name=="Bulbophyllum_Lindleyanum":
        st.info('''
    **กล้วยไม้สิงโตลินด์เลย์**  

    **ชื่อวิทยาศาสตร์** : Bulbophyllum lindleyanum 

    **สกุล** : กลอกตา (Bulbophyllum) 

    **ลักษณะทางพฤกษศาสตร์** : กล้วยไม้อิงอาศัย ลำลูกกล้วย ขนาด 2-2.5 ซม. มี 1 ใบที่ปลายลำ
    ใบรูปรีแกมขอบขนาน กว้าง 2-3 ซม. ยาว 10-13 ซม. ช่อดอกยาว 12-20 ซม. 
    ดอกกว้างประมาณ 4 มม. กลีบเลี้ยงสีขาว มีเส้นสีน้ำตาล ดำพาดกลางกลีบ 3 เส้น 
    และมีขนสีขาวปกคลุมทั่วกลีบ กลีบดอก สีขาวขนาดเล็ก มีขนบริเวณขอบกลีบ 
    กลางกลีบมีเส้นสีน้ำตาลดำ 1 เส้น กลีบปากรูปแถบ ด้านล่างกลีบมีขน 

    **วิธีการปลูก** : วัสดุที่เก็บความชื้นได้ดี โปร่ง ระบายน้ำและอากาศดี เช่น ถ่านทุบ 
    อิฐมอญทุบ กาบมะพร้าว รากเฟินชายผ้าสีดา เศษกระถางแตก หินภูเขาไฟ เป็นต้น   

    **การรดนํ้า** : รดน้ำสม่ำเสมอ ปริมาณน้ำที่พอดีไม่มากและไม่น้อยจนเกินไป 

    **แสงแดด** : แดดรำไร 

    **ขยายพันธุ์** : ขยายพันธ์ุโดยการแยกกอ ปักชำ หรือเพาะเลี้ยงเนื้อเยื่อ''')

    elif name=="Orchidaceae_Vandasanderiana":
        st.info('''
    **กล้วยไม้แวนด้าแซนเดอเรียน่า** 

    **ชื่อวิทยาศาสตร์** : Vanda sanderiana 

    **สกุล** : แวนด้า (Vanda) 

    **ลักษณะทางพฤกษศาสตร์** : แวนดามีความสูงของต้นได้ถึงหนึ่งเมตร ลำต้นตั้งตรง
    มีการเจริญเติบโตทางยอด ใบออกสลับซ้ายขวาเรียงซ้อนกันเป็นชั้นๆ ใบแบนยาวประมาณ 40 ซม.
    กว้าง 3 ซม .ที่ปลายใบเป็นรอยหยักแหว่งคล้ายรอยโดนแมลงกัด ก้านดอกตั้งตรง
    ในต้นที่สมบูรณ์แต่ละดอกรูปทรงกลมมีขนาดเส้นผ่านศูนย์กลางของทั้งดอกกว้างประมาณ 10 ซม.
    กลีบดอกนอกบนและกลีบดอกด้านในสองกลีบ มีขนาดยาวประมาณ 7 ซม .กว้าง 5.5 ซม. มีสีชมพูอ่อน
    และมีแต้มจุดกระสีน้ำตาลอยู่ช่วงกึ่งกลางดอก กลีบนอกด้านล่างสองกลีบ มีขนาด กว้าง 6.5 ซม .
    ยาวประมาณ 7 ซม . กลีบล่างมีสีน้ำตาลอมแดง มีลายเส้นในพื้นดอก ส่วนกลีบปากมีสีม่วงอมน้ำตาลเข้ม
    มีสันนูน 3 สันที่กลางกลีบปาก มีขนาด กว้างประมาณ 1.75 ซม. ยาวประมาณ 2.5 ซม    

    **วิธีการปลูก** : การปลูกมักนำไปปลูก ในกระถางแขวน ตอนแรก อาจใช้ออสมันดาเป็นเครื่องปลูกหรือ
    ใช้ถ่านรองกระถาง แต่ไม่ต้องใช้เครื่องปลูกเมื่อรากแข็งแรง ถ้าปลูกในสภาพแวดล้อมที่เหมาะสม 

    **การรดนํ้า** : ควรใช้น้ำที่สะอาดเช่นน้ำฝน  น้ำประปา หรือน้ำที่สะอาดอื่นๆ รดวันละครั้ง
    ค่าความเป็นกรดด่างขอน้ำ( PH) ควรอยู่ที่ 7.5 หรือต่ำกว่านั้นเล็กน้อย ในช่วงฤดูร้อนไม่ควรปล่อยให้ต้น
    กล้วยไม้แห้งหรือขาดน้ำ จนเกินไป เพราะกล้วยไม้ชนิดนี้เป็นกล้วยไม้รากอากาศ ในฤดูฝนควรเว้นระยะให้กล้วย
    ไม้ได้แห้งบ้าง และไม่จำเป็นต้องรดน้ำเพิ่มในช่วงที่มีฝนตกหนัก 

    **แสงแดด** : กล้วยไม้ชนิดนี้ชอบแสงปานกลางถึงแสงค่อนข้างมากประมาณ 60-70% หากเลี้ยงในโรงเรือนปิด
    ต้องมีแสงสว่างประมาณ2500-5000 แรงเทียนแต่ก็ไม่สามารถงอกงามได้ดีเหมือนแสงธรรมชาติ เมื่อใช้แสงจาก
    หลอดไฟ หากปลูกในบ้านควรจัดวางไว้ที่ใกล้หน้าต่างที่ได้แสง พอเพียง 

    **ขยายพันธุ์** : ขยายพันธ์ุโดยการแยกกอ ปักชำ หรือเพาะเลี้ยงเนื้อเยื่อ ''')

    elif name=="Orchidaceae_PhalaenopsisCornucervi":
        st.info('''
    **กล้วยไม้เอื้องเขากวางอ่อน/ต้นเขากวางอ่อน** 

    **ชื่อวิทยาศาสตร์** : Phalaenopsis cornucervi 

    **สกุล** : ฟาแลนน็อปซิส (Phalaenopsis) 

    **ลักษณะทางพฤกษศาสตร์** : ลำต้น เล็กและสั้นเรียว สูง 5-10 ซม. ใบ ใบรูปขอบขนานแกมรูปไข่กลับ
    ออกเรียงสลับระนาบเดียว กว้าง 2 – 4 เซนติเมตร ยาว 10 – 15 เซนติเมตร แผ่นใบหนาอวบน้ำ
    สีเขียวเป็นมัน ช่อดอกออกจากซอกใบ แต่ละช่อมี 5 – 8 ดอก  

    **วิธีการปลูก** : ใช้วัสดุรองระหว่างขอนไม้กับ เขากวางอ่อน เช่น กาบมะพร้าว หรือ สเฟกนั่มมอส
    หรือ รากชายผ้าสีดา ทั้งนี้เพื่อให้วัสดุปลูกเหล่านั้นคอยกักเก็บความชื้นให้กับ เขากวางอ่อน
    เพื่อให้กล้วยไม้โตเร็วและมีรากที่ สมบูรณ์ขึ้นกว่าเดิม   

    **การรดนํ้า** : รดน้ำวันละ 1 ครั้ง จะเช้าหรือเย็นแล้วแต่สะดวก หากจะให้ดีควรให้ปุ๋ยเป็นประจำทุกๆ
    1 สัปดาห์จะทำให้ กล้วยไม้ของเรา แข็งแรง สวยงาม มากยิ่งขึ้น 

    **แสงแดด** : นำกล้วยไม้ที่ปลูกใหม่นี้แขวนไว้ในร่มรำไร อย่าร่มมากเกินไป เช่น
    ใต้โรงรถยนต์ หรือบริเวณที่ทึบ ควรแขวนอยู่ ในบริเวณที่ที่โปร่ง มีแสงสว่างทอดถึง หรือใต้แสลน 80% 

    **ขยายพันธุ์** : ขยายพันธ์ุโดยการแยกกอหรือเพาะเลี้ยงเนื้อเยื่อ  ''')

    elif name=="Orchidaceae_BulbphyllumGracillimum":
        st.info('''
    **กล้วยไม้สิงโตพู่รัศมี/สิงโตเคราแดง** 

    **ชื่อวิทยาศาสตร์** : Bulbphyllum gracillimum 

    **สกุล** : สิงโตพัด (Cirrhopetalum) 

    **ลักษณะทางพฤกษศาสตร์** : ลำต้น ลำลูกกล้วยรูปไข่แกมรูปขอบขนาน ขนาด 1.5 – 2 เซนติเมตร
    ใบรูปแถบ กว้าง 2.5 เซนติเมตร ยาว 12 เซนติเมตร มีเพียงใบเดียว ก้านช่อดอกยาวกว่าความยาวใบ
    ดอกสีม่วงแดง มีดอกย่อย  15 – 20 ดอกดอกขนาด 0.5 – 1 เซนติเมตร
    ยาว 3 – 4 เซนติเมตร กลีบดอกสีแดงสด โคนกลีบสีขาว กลีบเลี้ยงคู่ข้างเรียวและยื่นยาวมาก
    กลีบปากสีขาวเหลือบชมพู โคนสีม่วงอมชมพู   

    **วิธีการปลูก** : วัสดุที่เก็บความชื้นได้ดี โปร่ง ระบายน้ำและอากาศดี เช่น ถ่านทุบ อิฐมอญทุบ กาบมะพร้าว
    รากเฟินชายผ้าสีดา เศษกระถางแตก หินภูเขาไฟ  
    
    **การรดนํ้า** : รดน้ำสม่ำเสมอ ปริมาณน้ำที่พอดีไม่มากและไม่น้อยจนเกินไป  
    
    **แสงแดด** : รำไร หรือได้รับแสงในช่วงเช้า  
    
    **ขยายพันธุ์** : ขยายพันธุ์โดยการแยกกอ ปักชำ หรือเพาะเลี้ยงเนื้อเยื่อ ''')

    elif name=="Orchidaceae_AeridesFlabellata":
        st.info('''
    **กล้วยไม้สายพันธุ์กุหลาบอินทจักร/เอื้องอินทจักร** 

    **ชื่อวิทยาศาสตร์** : Aerides flabellata 

    **สกุล** : กุหลาบ (Aerides) 
    
    **ลักษณะทางพฤกษศาสตร์** : ลำต้น ยาว 12-20 เซนติเมตร ใบเรียงกันค่อนข้างแน่น
    ใบรูปขอบขนานแกมรูปรี ขนาด 10-12 x 1.8-2 เซนติเมตร แผ่นใบหนาและเหนียว มักพับเป็นรางผิวใบแห้ง
    ดอก ออกเป็นช่อตั้งหรือเอนออกจากต้น ช่อละ 5-10 ดอก ช่อโปร่ง กลีบเลี้ยงและกลีบดอกมีลักษณะคล้ายกัน
    มีจุดสีน้ำตาลหนาแน่น กลีบปากหยักเว้าเป็น 3 หยัก หยักกลางแผ่กว้าง สีขาว มีจุดสีชมพูอมม่วง
    ขอบจักฟันเลื่อยอีก 2 หยักด้านข้างกระดกขึ้น สีเดียวกับกลีบเลี้ยงและกลีบดอก มีเดือยทางด้านหลัง
    ดอกขนาด 1.2-1.5 x 3 เซนติเมตร  

    **วิธีการปลูก** : วัสดุที่เก็บความชื้นได้ดี โปร่ง ระบายน้ำและอากาศดี เช่น ถ่านทุบ อิฐมอญทุบ
    กาบมะพร้าว รากเฟินชายผ้าสีดา เศษกระถางแตก หินภูเขาไฟ 
    
    **การรดนํ้า** : รดน้ำสม่ำเสมอ ปริมาณน้ำที่พอดีไม่มากและไม่น้อยจนเกินไป 
    
    **แสงแดด** : รำไร หรือได้รับแสงในช่วงเช้า 
    
    **การขยายพันธุ์** : ขยายพันธุ์โดยการแยกกอหรือเพาะเลี้ยงเนื้อเยื่อ ''')

    elif name=="Orchidaceae_Ludisia":
        st.info('''
    **กล้วยไม้สายพันธุ์ว่านน้ำทอง** 

    **ชื่อวิทยาศาสตร์** : Ludisia discolor  
    
    **สกุล** : ว่านน้ำทอง (Aerides) 
    
    **ลักษณะทางพฤกษศาสตร์** : ลำต้นเป็นพืชกึ่งเลื้อย มีลำต้นตั้งตรงหรือโน้มเอียงลาดตามพื้น ลำต้นมีลักษณะอวบน้ำ
    และมีขนอ่อนปกคลุม ลำต้นสูงประมาณ 10-15 เซนติเมตร ใบว่านน้ำทองออกเป็นใบเดี่ยว ออกเรียงเวียน
    สลับตรงกันข้ามกันสี่ด้าน ใบว่านน้ำทองมีรูปไข่หรือรูปหอก กว้างประมาณ 2-2.5 เซนติเมตร
    ยาวประมาณ 4-6.5 เซนติเมตร แผ่นใบและขอบใบเรีย แผ่นใบมีสีน้ำตาลอมดำ หรือ สีเขียว
    และมีลายประสีขาวของเส้นใบ และเส้นแขนงใบ ดอกเป็นช่อตรงกลางยอดยาวประมาณ 12-15 เซนติเมตร
    ช่อดอกประกอบด้วยดอกย่อยเรียงสลับกันตามความสูงของก้านช่อดอก จำนวน 12-20 ดอก  
    
    **วิธีการปลูก** : กระถางที่ใช้ในการปลูกส่วนใหญ่จะเป็นทรงกว้างมากกว่าทรงสูงเนื่องจากกล้วยไม้
    เจริญเติบโตทางด้านข้างส่วนวัสดุที่นิยมนำมาใช้ปลูก คือ ดิน 50% และเปลือกไม้อีก 50%
    ว่านน้ำทองเป็นพืชที่เติบโตได้ดีในดินร่วนซุย ชุ่มชื้น และมีอินทรีย์วัตถุสูง 
    นิยมปลูกในแปลงจัดสวนเป็นไม้ประดับระดับล่างหรือปลูกในกระถางสำหรับวางประดับ 
    
    **การรดนํ้า** : รดน้ำวันละ 1 ครั้ง หรือ สามารถรดน้ำให้ชุ่มเครื่องปลูก แล้วทิ้งไว้ได้ 2-3 วัน 
    
    **แสงแดด** : ปลูกกล้วยไม้ไว้ในร่ม ถ้ากล้วยไม้ถูกแดดมากเกินไป ใบเป็นสีแดง
    กล้วยไม้ต้องการความชื้นสูงตลอดไป มันทนสภาพอากาศได้หลากหลายพอสมควร
    ในฤดูร้อนกล้วยไม้อาจทนความร้อนได้สูงถึง 35 องศา ส่วนในฤดูหนาวกล้วยไม้ทนได้ในอุณหภูมิ 5 องศา 
    
     **การขยายพันธุ์** : ขยายพันธุ์โดยการปักชำต้น ด้วยการตัดต้น ยาว 15-20 เซนติเมตร
     ปักชำในแปลงหรือในกระถาง รดน้ำให้ชุ่มทุกวัน ซึ่งต้นปักชำจะติดรากประมาณ 10-20 วัน ''')

    elif name=="Orchidaceae_PaphiopedilumCallosum":
        st.info('''
    **กล้วยไม้สายพันธุ์รองเท้านารีคางกบ** 

    **ชื่อวิทยาศาสตร์** : Paphiopedilum callosum  
    
    **สกุล** : รองเท้านารี (Paphiopedilum) 
    
    **ลักษณะทางพฤกษศาสตร์** : กล้วยไม้ขึ้นตามพื้นดินใบรูปขอบขนานหรือแกมรูปไข่กลับ ยาว 10–20 ซม.
    ช่อดอกมี 1–2 ดอก ก้านช่อยาว 12–25 ซม. ใบประดับรูปไข่ ปลายแหลม ยาว 1.5–2.8 ซม.
    ดอกสีขาวอมเขียวหรือน้ำตาล เส้นกลีบสีม่วง กลีบเลี้ยงบนรูปไข่กว้างเกือบกลม กว้าง 4.2–6 ซม.
    ปลายกลีบเป็นติ่งแหลม กลีบคู่ข้างรูปรี เว้า ยาว 2.7–3.2 ซม. กลีบดอกรูปลิ้น ยาว 4.6–6.8 ซม.
    บิดเล็กน้อย ปลายกลีบมนหรือกลม ขอบกลีบบน และล่างมักมีจุดสีน้ำตาลแดง ถุงกลีบปากสีเขียวอมน้ำตาล
    ยาว 2.5–4.5 ซม. ขอบด้านในมีต่อม แผ่นเกสรเพศผู้ ที่เป็นหมันรูปรี ยาวประมาณ 1 ซม.
    ปลายจักโค้งคล้ายรูปเคียว มีขนสั้นนุ่ม รังไข่รวมก้านยาว 3–6.5 ซม. 
    
    **วิธีการปลูก** : ควรปลูกในโรงเรือนที่มีการพรางแสง ถ้าจะให้ดีควรมีหลังคากันฝน อากาศถ่ายเทได้สะดวก
    รดน้ำสม่ำเสมอ ปลูกในกระถางพลาสติก หรือกระถางดินเผา วัสดุปลูกที่ควรระบายน้ำได้ดี เก็บความชื้นได้ดี
    ทนทาน ที่นิยมใช้ได้แก่ โฟม ถ่านกาบมะพร้าวสับ ออสมันด้า ใบทองหลาง ใบก้ามปูผุ 
    
    **การรดนํ้า** : รดน้ำวันละ 1 ครั้ง ในตอนเช้า 
    
    **แสงแดด** : รำไร หรือได้รับแสงในช่วงเช้า  
    
    **การขยายพันธุ์** : ขยายพันธุ์โดยการแยกกอ ปักชำ หรือเพาะเลี้ยงเนื้อเยื่อ ''')

    elif name=="Orchidaceae_BulbophyllumFlabellumVeneris":
        st.info('''
    **กล้วยไม้สายพันธุ์สิงโตพัดแดง** 

    **ชื่อวิทยาศาสตร์** : Bulbophyllum flabellum-veneris  
    
    **สกุล** : สิงโตกลอกตา (Bulbophyllum) 
    
    **ลักษณะทางพฤกษศาสตร์** : มีลำลูกกล้วยขนาดเล็ก รูปไข่ยอดแหลมซึ่งเกิดระหว่าง
    ไหลช่วงระยะห่าง 0.5-1 ซม.ขนาดลำลูกกล้วย มีความสูงประมาณ 1.5 ซม. กว้างประมาณ 1.3 ซม.
    มีใบเดี่ยวยาวรีกว้าง 2-3 ซม.ใบยาวประมาณ 9-13 ซม. ก้านดอกเล็กเรียวยาว 7-14 ซม.
    ก้านดอกสีม่วงอมแดง เกิดจากตาดอกที่โคนลำลูกกล้วย มีดอกขนาดเล็ก สีตั้งแต่ม่วงแดงอ่อนๆไปจนถึงสีเข้มจัด
    มีดอกในช่อ จำนวน 12  ดอก 
    
    **วิธีการปลูก** : วัสดุที่เก็บความชื้นได้ดี โปร่ง ระบายน้ำและอากาศดี เช่น ถ่านทุบ อิฐมอญทุบ กาบมะพร้าว
    รากเฟินชายผ้าสีดา เศษกระถางแตก หินภูเขาไฟ เป็นต้น 
    
    **การรดนํ้า** : รดปานกลาง ไม่เยอะและไม่น้อยจนเกินไป 
    
    **แสงแดด** : รำไร หรือได้รับแสงในช่วงเช้า  
    
    **การขยายพันธุ์** : ขยายพันธุ์โดยการแยกกอ ปักชำ หรือเพาะเลี้ยงเนื้อเยื่อ ''')

# function predict รูป
def predict(image,device):
    return model(image,imgsz=640,device=device)[0]

# function show รูปต้นฉบับและรูปที่ predict หลังจากนั้น show information
def show_predict(image):
    image = Image.open(image)
    col1.write("Original image")
    col1.image(image)
    try:
        results=predict(image,device_type)
    except:
        results=predict(image,"cpu")
    if len(results)!=0:
        col2.write("Predicted image")
        col2.image(results.plot()[:, :, ::-1])
        classes = results.boxes.cls.cpu().tolist()
        names = results.names
        confs = results.boxes.conf.float().cpu().tolist()
        final_class=names[mode(classes)]
        col2.success(f"{final_class} : {round(mean(confs),2)}")
        show_information(final_class)
    else:
        col2.write("Predicted image")
        col2.image(image)
        col2.success("Predicted: Unknown")
        col2.error("ไม่พบข้อมูล")



#โหลด model
model=load_model("./best.pt")
#เขียนข้อความที่ show ใน streamlit
with st.sidebar:
    selected=option_menu(
        menu_title="Menu",
        options=["Option"],
        icons=["gear-fill"],
        menu_icon=["house door fill"],
        default_index=0,
    )

    if selected == "Option":
            st.title(f"Welcome to {selected} page")
            source_type = st.sidebar.radio("Select Menu", ["From test set", "Upload your own data","Orchid information"])
            device_type = st.sidebar.radio("Select compute device", ["cpu", "cuda"])
            st.sidebar.write("👆🏻: เลือกหัวข้อที่ต้องการ")

st.write("## Classification of orchids")
st.write(":point_left: Select options left-haned menu bar.")

#ถ้าเลือก upload data
if source_type=="Upload your own data":
    my_upload = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    p=st.button("predict")
    #เมื่อกดปุ่ม predict และ upload
    if my_upload is not None and p:
        col1,col2=st.columns(2)
        show_predict(my_upload)
# ถ้าเลือก test set
elif source_type=="From test set":
    list_images=os.listdir("images")
    number = st.slider("Select random image from test set", min_value=0, max_value=len(list_images)-1, value=int((len(list_images)-1)/2))
    p=st.button("predict")
    col1,col2=st.columns(2)
    #เมื่อกดปุ่ม predict
    if  p:
        show_predict("images/"+list_images[number])\

elif source_type=="Orchid information":
    selected_option = st.selectbox("เลือกสายพันธุ์กล้วยไม้",
                                   ["", "กล้วยไม้เข็มหนู", "กล้วยไม้เอื้องเงินหลวง", "กล้วยไม้สิงโตลินด์เลย์" , "กล้วยไม้แวนด้าแซนเดอเรียน่า"
                                    , "กล้วยไม้เอื้องเขากวางอ่อน", "กล้วยไม้สิงโตพู่รัศมี", "กล้วยไม้กุหลาบอินทรจักร", "กล้วยไม้ว่านนํ้าทอง", "กล้วยไม้รองเท้านารีคางกบ",
                                    "กล้วยไม้สิงโตพัดแดง"])
    st.write("You Selected:", selected_option)

    if selected_option == "กล้วยไม้เข็มหนู":
        st.image("เข็มหนู.jpg", caption="ตัวอย่างรูปภาพกล้วยไม้สายพันธุ์เข็มหนู", use_column_width=True)
        st.success('''
        **กล้วยไม้เข็มหนู/กุหลาบดง**

        **ชื่อวิทยาศาสตร์** : Smitinandiamicrantha

        **สกุล** : เข็ม (Ascocentrum)

        **ลักษณะทางพฤกษศาสตร์** : เป็นกล้วยไม้ที่มีใบเป็นแบบใบกลม มีร่องลึกทางด้านบนของใบ 
        ใบกว้างประมาณ 5 มิลลิเมตร มีดอกสีม่วงอ่อนช่อดอกตั้งหรือเอนเล็กน้อย ยาวใกล้เคียงใบ 
        ดอกในช่อโปร่ง ขนาดดอก 0.6-1เซนติเมตร   

        **วิธีการปลูก** : ปลูกในกระถาง ติดแผ่นไม้ วัสดุปลูกที่ใช้เช่น กาบมะพร้าวสับ 
        หากปลูกติดกิ่งหรือลำต้นควรเลือกต้น ที่มีเปลือกที่สามารถดูดซับความชื้นได้ดี
        ทรงพุ่มไม่หนาทึบ อากาศถ่ายเทสะดวก    

        **การรดนํ้า** : รดน้ำสม่ำเสมอ ปริมาณน้ำที่พอดีไม่มากและไม่น้อยจนเกินไป 

        **แสงแดด** : แดดรำไร 

        **ขยายพันธุ์** : ขยายพันธ์ุโดยการแบ่งกอ หรือเพาะเมล็ด ''')

    elif selected_option == "กล้วยไม้เอื้องเงินหลวง":
        st.image("เอื้องเงินหลวง.jpg", caption="ตัวอย่างรูปภาพกล้วยไม้เอื้องเงินหลวง", use_column_width=True)
        st.success('''
               **กล้วยไม้เอื้องเงินหลวง/เอื้องตาเหิน**

               **ชื่อวิทยาศาสตร์** : Dendrobium formosum

               **สกุล** : หวาย (Dendrobium) 

               **ลักษณะทางพฤกษศาสตร์** : เป็นกล้วยไม้อิงอาศัย สูง 25-50 ซม. ลำต้นรูปแท่งดินสอกลม 
               โคนเรียวและคอด ก้านใบมีขนสีดำ ใบเป็นรูปรีแกมรูปขอบขนาน  กว้างประมาณ 2-2.5 ซม. 
               ยาว 6-8 ซม. ออกเรียงสลับตามข้อลำต้น ปลายและโคนใบแหลม สีเขียวสดเป็นมันและมักจะทิ้งใบเวลาผลิดอก   

               **วิธีการปลูก** : ใช้วัสดุที่เก็บความชื้นได้ดี โปร่ง ระบายน้ำและอากาศดี เช่น ถ่านทุบ 
               อิฐมอญทุบ กาบมะพร้าว รากเฟินชายผ้าสีดา เศษกระถางแตก หินภูเขาไฟ เป็นต้น 

               **การรดนํ้า** : รดน้ำปานกลาง ไม่มากและน้อยจนเกินไป 

               **แสงแดด** : แดดรำไร หรือได้รับแสงในช่วงเช้า 

               **ขยายพันธุ์** : ขยายพันธุ์โดยการแยกกอหรือเพาะเลี้ยงเนื้อเยื่อ''')

    elif selected_option == "กล้วยไม้สิงโตลินด์เลย์":
        st.image("สิงโตลินด์เลย์.jpg", caption="ตัวอย่างรูปภาพกล้วยไม้สิงโตลินด์เลย์", use_column_width=True)
        st.success('''
        **กล้วยไม้สิงโตลินด์เลย์**

        **ชื่อวิทยาศาสตร์** : Bulbophyllum lindleyanum 
    
        **สกุล** : กลอกตา (Bulbophyllum) 
    
        **ลักษณะทางพฤกษศาสตร์** : กล้วยไม้อิงอาศัย ลำลูกกล้วย ขนาด 2-2.5 ซม. มี 1 ใบที่ปลายลำ
        ใบรูปรีแกมขอบขนาน กว้าง 2-3 ซม. ยาว 10-13 ซม. ช่อดอกยาว 12-20 ซม. 
        ดอกกว้างประมาณ 4 มม. กลีบเลี้ยงสีขาว มีเส้นสีน้ำตาล ดำพาดกลางกลีบ 3 เส้น 
        และมีขนสีขาวปกคลุมทั่วกลีบ กลีบดอก สีขาวขนาดเล็ก มีขนบริเวณขอบกลีบ 
        กลางกลีบมีเส้นสีน้ำตาลดำ 1 เส้น กลีบปากรูปแถบ ด้านล่างกลีบมีขน 
    
        **วิธีการปลูก** : วัสดุที่เก็บความชื้นได้ดี โปร่ง ระบายน้ำและอากาศดี เช่น ถ่านทุบ 
        อิฐมอญทุบ กาบมะพร้าว รากเฟินชายผ้าสีดา เศษกระถางแตก หินภูเขาไฟ เป็นต้น   
    
        **การรดนํ้า** : รดน้ำสม่ำเสมอ ปริมาณน้ำที่พอดีไม่มากและไม่น้อยจนเกินไป 
    
        **แสงแดด** : แดดรำไร 
    
        **ขยายพันธุ์** : ขยายพันธ์ุโดยการแยกกอ ปักชำ หรือเพาะเลี้ยงเนื้อเยื่อ''')


    elif selected_option == "กล้วยไม้แวนด้าแซนเดอเรียน่า":
        st.image("แวนด้าแซนเดอเรียน่า.jpg", caption="ตัวอย่างรูปภาพกล้วยไม้แวนด้าแซนเดอเรียน่า", use_column_width=True)
        st.success('''
            **กล้วยไม้แวนด้าแซนเดอเรียน่า**

            **ชื่อวิทยาศาสตร์** : Vanda sanderiana 

            **สกุล** : แวนด้า (Vanda) 

            **ลักษณะทางพฤกษศาสตร์** : แวนดามีความสูงของต้นได้ถึงหนึ่งเมตร ลำต้นตั้งตรง
            มีการเจริญเติบโตทางยอด ใบออกสลับซ้ายขวาเรียงซ้อนกันเป็นชั้นๆ ใบแบนยาวประมาณ 40 ซม.
            กว้าง 3 ซม .ที่ปลายใบเป็นรอยหยักแหว่งคล้ายรอยโดนแมลงกัด ก้านดอกตั้งตรง
            ในต้นที่สมบูรณ์แต่ละดอกรูปทรงกลมมีขนาดเส้นผ่านศูนย์กลางของทั้งดอกกว้างประมาณ 10 ซม.
            กลีบดอกนอกบนและกลีบดอกด้านในสองกลีบ มีขนาดยาวประมาณ 7 ซม .กว้าง 5.5 ซม. มีสีชมพูอ่อน
            และมีแต้มจุดกระสีน้ำตาลอยู่ช่วงกึ่งกลางดอก กลีบนอกด้านล่างสองกลีบ มีขนาด กว้าง 6.5 ซม .
            ยาวประมาณ 7 ซม . กลีบล่างมีสีน้ำตาลอมแดง มีลายเส้นในพื้นดอก ส่วนกลีบปากมีสีม่วงอมน้ำตาลเข้ม
            มีสันนูน 3 สันที่กลางกลีบปาก มีขนาด กว้างประมาณ 1.75 ซม. ยาวประมาณ 2.5 ซม    

            **วิธีการปลูก** : การปลูกมักนำไปปลูก ในกระถางแขวน ตอนแรก อาจใช้ออสมันดาเป็นเครื่องปลูกหรือ
            ใช้ถ่านรองกระถาง แต่ไม่ต้องใช้เครื่องปลูกเมื่อรากแข็งแรง ถ้าปลูกในสภาพแวดล้อมที่เหมาะสม 

            **การรดนํ้า** : ควรใช้น้ำที่สะอาดเช่นน้ำฝน  น้ำประปา หรือน้ำที่สะอาดอื่นๆ รดวันละครั้ง
            ค่าความเป็นกรดด่างขอน้ำ( PH) ควรอยู่ที่ 7.5 หรือต่ำกว่านั้นเล็กน้อย ในช่วงฤดูร้อนไม่ควรปล่อยให้ต้น
            กล้วยไม้แห้งหรือขาดน้ำ จนเกินไป เพราะกล้วยไม้ชนิดนี้เป็นกล้วยไม้รากอากาศ ในฤดูฝนควรเว้นระยะให้กล้วย
            ไม้ได้แห้งบ้าง และไม่จำเป็นต้องรดน้ำเพิ่มในช่วงที่มีฝนตกหนัก 

            **แสงแดด** : กล้วยไม้ชนิดนี้ชอบแสงปานกลางถึงแสงค่อนข้างมากประมาณ 60-70% หากเลี้ยงในโรงเรือนปิด
            ต้องมีแสงสว่างประมาณ2500-5000 แรงเทียนแต่ก็ไม่สามารถงอกงามได้ดีเหมือนแสงธรรมชาติ เมื่อใช้แสงจาก
            หลอดไฟ หากปลูกในบ้านควรจัดวางไว้ที่ใกล้หน้าต่างที่ได้แสง พอเพียง 

            **ขยายพันธุ์** : ขยายพันธ์ุโดยการแยกกอ ปักชำ หรือเพาะเลี้ยงเนื้อเยื่อ ''')

    elif selected_option == "กล้วยไม้เอื้องเขากวางอ่อน":
            st.image("เอื้องเขากวางอ่อน.jpg", caption="ตัวอย่างรูปภาพกล้วยไม้เอื้องเขากวางอ่อน", use_column_width=True)
            st.success('''
            **กล้วยไม้เอื้องเขากวางอ่อน/ต้นเขากวางอ่อน**

            **ชื่อวิทยาศาสตร์** : Phalaenopsis cornucervi 
        
            **สกุล** : ฟาแลนน็อปซิส (Phalaenopsis) 
        
            **ลักษณะทางพฤกษศาสตร์** : ลำต้น เล็กและสั้นเรียว สูง 5-10 ซม. ใบ ใบรูปขอบขนานแกมรูปไข่กลับ
            ออกเรียงสลับระนาบเดียว กว้าง 2 – 4 เซนติเมตร ยาว 10 – 15 เซนติเมตร แผ่นใบหนาอวบน้ำ
            สีเขียวเป็นมัน ช่อดอกออกจากซอกใบ แต่ละช่อมี 5 – 8 ดอก  
        
            **วิธีการปลูก** : ใช้วัสดุรองระหว่างขอนไม้กับ เขากวางอ่อน เช่น กาบมะพร้าว หรือ สเฟกนั่มมอส
            หรือ รากชายผ้าสีดา ทั้งนี้เพื่อให้วัสดุปลูกเหล่านั้นคอยกักเก็บความชื้นให้กับ เขากวางอ่อน
            เพื่อให้กล้วยไม้โตเร็วและมีรากที่ สมบูรณ์ขึ้นกว่าเดิม   
        
            **การรดนํ้า** : รดน้ำวันละ 1 ครั้ง จะเช้าหรือเย็นแล้วแต่สะดวก หากจะให้ดีควรให้ปุ๋ยเป็นประจำทุกๆ
            1 สัปดาห์จะทำให้ กล้วยไม้ของเรา แข็งแรง สวยงาม มากยิ่งขึ้น 
        
            **แสงแดด** : นำกล้วยไม้ที่ปลูกใหม่นี้แขวนไว้ในร่มรำไร อย่าร่มมากเกินไป เช่น
            ใต้โรงรถยนต์ หรือบริเวณที่ทึบ ควรแขวนอยู่ ในบริเวณที่ที่โปร่ง มีแสงสว่างทอดถึง หรือใต้แสลน 80% 
        
            **ขยายพันธุ์** : ขยายพันธ์ุโดยการแยกกอหรือเพาะเลี้ยงเนื้อเยื่อ  ''')


    elif selected_option == "กล้วยไม้สิงโตพู่รัศมี":
        st.image("สิงโตพู่รัศมี.jpg", caption="ตัวอย่างรูปภาพกล้วยไม้สิงโตพู่รัศมี", use_column_width=True)
        st.success('''
            **กล้วยไม้สิงโตพู่รัศมี/สิงโตเคราแดง**

            **ชื่อวิทยาศาสตร์** : Bulbphyllum gracillimum 

            **สกุล** : สิงโตพัด (Cirrhopetalum) 

            **ลักษณะทางพฤกษศาสตร์** : ลำต้น ลำลูกกล้วยรูปไข่แกมรูปขอบขนาน ขนาด 1.5 – 2 เซนติเมตร
            ใบรูปแถบ กว้าง 2.5 เซนติเมตร ยาว 12 เซนติเมตร มีเพียงใบเดียว ก้านช่อดอกยาวกว่าความยาวใบ
            ดอกสีม่วงแดง มีดอกย่อย  15 – 20 ดอกดอกขนาด 0.5 – 1 เซนติเมตร
            ยาว 3 – 4 เซนติเมตร กลีบดอกสีแดงสด โคนกลีบสีขาว กลีบเลี้ยงคู่ข้างเรียวและยื่นยาวมาก
            กลีบปากสีขาวเหลือบชมพู โคนสีม่วงอมชมพู   

            **วิธีการปลูก** : วัสดุที่เก็บความชื้นได้ดี โปร่ง ระบายน้ำและอากาศดี เช่น ถ่านทุบ อิฐมอญทุบ กาบมะพร้าว
            รากเฟินชายผ้าสีดา เศษกระถางแตก หินภูเขาไฟ  

            **การรดนํ้า** : รดน้ำสม่ำเสมอ ปริมาณน้ำที่พอดีไม่มากและไม่น้อยจนเกินไป  

            **แสงแดด** : รำไร หรือได้รับแสงในช่วงเช้า  

            **ขยายพันธุ์** : ขยายพันธุ์โดยการแยกกอ ปักชำ หรือเพาะเลี้ยงเนื้อเยื่อ ''')


    elif selected_option == "กล้วยไม้กุหลาบอินทรจักร":
        st.image("กุหลาบอินทรจักร.jpg", caption="ตัวอย่างรูปภาพกล้วยไม้กุหลาบอินทรจักร", use_column_width=True)
        st.success('''
            **กล้วยไม้สายพันธุ์กุหลาบอินทจักร/เอื้องอินทจักร** 

            **ชื่อวิทยาศาสตร์** : Aerides flabellata 
        
            **สกุล** : กุหลาบ (Aerides) 
            
            **ลักษณะทางพฤกษศาสตร์** : ลำต้น ยาว 12-20 เซนติเมตร ใบเรียงกันค่อนข้างแน่น
            ใบรูปขอบขนานแกมรูปรี ขนาด 10-12 x 1.8-2 เซนติเมตร แผ่นใบหนาและเหนียว มักพับเป็นรางผิวใบแห้ง
            ดอก ออกเป็นช่อตั้งหรือเอนออกจากต้น ช่อละ 5-10 ดอก ช่อโปร่ง กลีบเลี้ยงและกลีบดอกมีลักษณะคล้ายกัน
            มีจุดสีน้ำตาลหนาแน่น กลีบปากหยักเว้าเป็น 3 หยัก หยักกลางแผ่กว้าง สีขาว มีจุดสีชมพูอมม่วง
            ขอบจักฟันเลื่อยอีก 2 หยักด้านข้างกระดกขึ้น สีเดียวกับกลีบเลี้ยงและกลีบดอก มีเดือยทางด้านหลัง
            ดอกขนาด 1.2-1.5 x 3 เซนติเมตร  
        
            **วิธีการปลูก** : วัสดุที่เก็บความชื้นได้ดี โปร่ง ระบายน้ำและอากาศดี เช่น ถ่านทุบ อิฐมอญทุบ
            กาบมะพร้าว รากเฟินชายผ้าสีดา เศษกระถางแตก หินภูเขาไฟ 
            
            **การรดนํ้า** : รดน้ำสม่ำเสมอ ปริมาณน้ำที่พอดีไม่มากและไม่น้อยจนเกินไป 
            
            **แสงแดด** : รำไร หรือได้รับแสงในช่วงเช้า 
            
            **การขยายพันธุ์** : ขยายพันธุ์โดยการแยกกอหรือเพาะเลี้ยงเนื้อเยื่อ ''')


    elif selected_option == "กล้วยไม้ว่านนํ้าทอง":
        st.image("ว่านน้ำทอง.jpg", caption="ตัวอย่างรูปภาพกล้วยไม้ว่านนํ้าทอง", use_column_width=True)
        st.success('''
            **กล้วยไม้สายพันธุ์ว่านน้ำทอง** 

            **ชื่อวิทยาศาสตร์** : Ludisia discolor  
            
            **สกุล** : ว่านน้ำทอง (Aerides) 
            
            **ลักษณะทางพฤกษศาสตร์** : ลำต้นเป็นพืชกึ่งเลื้อย มีลำต้นตั้งตรงหรือโน้มเอียงลาดตามพื้น ลำต้นมีลักษณะอวบน้ำ
            และมีขนอ่อนปกคลุม ลำต้นสูงประมาณ 10-15 เซนติเมตร ใบว่านน้ำทองออกเป็นใบเดี่ยว ออกเรียงเวียน
            สลับตรงกันข้ามกันสี่ด้าน ใบว่านน้ำทองมีรูปไข่หรือรูปหอก กว้างประมาณ 2-2.5 เซนติเมตร
            ยาวประมาณ 4-6.5 เซนติเมตร แผ่นใบและขอบใบเรีย แผ่นใบมีสีน้ำตาลอมดำ หรือ สีเขียว
            และมีลายประสีขาวของเส้นใบ และเส้นแขนงใบ ดอกเป็นช่อตรงกลางยอดยาวประมาณ 12-15 เซนติเมตร
            ช่อดอกประกอบด้วยดอกย่อยเรียงสลับกันตามความสูงของก้านช่อดอก จำนวน 12-20 ดอก  
            
            **วิธีการปลูก** : กระถางที่ใช้ในการปลูกส่วนใหญ่จะเป็นทรงกว้างมากกว่าทรงสูงเนื่องจากกล้วยไม้
            เจริญเติบโตทางด้านข้างส่วนวัสดุที่นิยมนำมาใช้ปลูก คือ ดิน 50% และเปลือกไม้อีก 50%
            ว่านน้ำทองเป็นพืชที่เติบโตได้ดีในดินร่วนซุย ชุ่มชื้น และมีอินทรีย์วัตถุสูง 
            นิยมปลูกในแปลงจัดสวนเป็นไม้ประดับระดับล่างหรือปลูกในกระถางสำหรับวางประดับ 
            
            **การรดนํ้า** : รดน้ำวันละ 1 ครั้ง หรือ สามารถรดน้ำให้ชุ่มเครื่องปลูก แล้วทิ้งไว้ได้ 2-3 วัน 
            
            **แสงแดด** : ปลูกกล้วยไม้ไว้ในร่ม ถ้ากล้วยไม้ถูกแดดมากเกินไป ใบเป็นสีแดง
            กล้วยไม้ต้องการความชื้นสูงตลอดไป มันทนสภาพอากาศได้หลากหลายพอสมควร
            ในฤดูร้อนกล้วยไม้อาจทนความร้อนได้สูงถึง 35 องศา ส่วนในฤดูหนาวกล้วยไม้ทนได้ในอุณหภูมิ 5 องศา 
            
             **การขยายพันธุ์** : ขยายพันธุ์โดยการปักชำต้น ด้วยการตัดต้น ยาว 15-20 เซนติเมตร
             ปักชำในแปลงหรือในกระถาง รดน้ำให้ชุ่มทุกวัน ซึ่งต้นปักชำจะติดรากประมาณ 10-20 วัน ''')


    elif selected_option == "กล้วยไม้รองเท้านารีคางกบ":
        st.image("รองเท้านารีคางกบ.jpg", caption="ตัวอย่างรูปภาพกล้วยไม้รองเท้านารีคางกบ", use_column_width=True)
        st.success('''
            **กล้วยไม้สายพันธุ์รองเท้านารีคางกบ**

            **ชื่อวิทยาศาสตร์** : Paphiopedilum callosum  
            
            **สกุล** : รองเท้านารี (Paphiopedilum) 
            
            **ลักษณะทางพฤกษศาสตร์** : กล้วยไม้ขึ้นตามพื้นดินใบรูปขอบขนานหรือแกมรูปไข่กลับ ยาว 10–20 ซม.
            ช่อดอกมี 1–2 ดอก ก้านช่อยาว 12–25 ซม. ใบประดับรูปไข่ ปลายแหลม ยาว 1.5–2.8 ซม.
            ดอกสีขาวอมเขียวหรือน้ำตาล เส้นกลีบสีม่วง กลีบเลี้ยงบนรูปไข่กว้างเกือบกลม กว้าง 4.2–6 ซม.
            ปลายกลีบเป็นติ่งแหลม กลีบคู่ข้างรูปรี เว้า ยาว 2.7–3.2 ซม. กลีบดอกรูปลิ้น ยาว 4.6–6.8 ซม.
            บิดเล็กน้อย ปลายกลีบมนหรือกลม ขอบกลีบบน และล่างมักมีจุดสีน้ำตาลแดง ถุงกลีบปากสีเขียวอมน้ำตาล
            ยาว 2.5–4.5 ซม. ขอบด้านในมีต่อม แผ่นเกสรเพศผู้ ที่เป็นหมันรูปรี ยาวประมาณ 1 ซม.
            ปลายจักโค้งคล้ายรูปเคียว มีขนสั้นนุ่ม รังไข่รวมก้านยาว 3–6.5 ซม. 
            
            **วิธีการปลูก** : ควรปลูกในโรงเรือนที่มีการพรางแสง ถ้าจะให้ดีควรมีหลังคากันฝน อากาศถ่ายเทได้สะดวก
            รดน้ำสม่ำเสมอ ปลูกในกระถางพลาสติก หรือกระถางดินเผา วัสดุปลูกที่ควรระบายน้ำได้ดี เก็บความชื้นได้ดี
            ทนทาน ที่นิยมใช้ได้แก่ โฟม ถ่านกาบมะพร้าวสับ ออสมันด้า ใบทองหลาง ใบก้ามปูผุ 
            
            **การรดนํ้า** : รดน้ำวันละ 1 ครั้ง ในตอนเช้า 
            
            **แสงแดด** : รำไร หรือได้รับแสงในช่วงเช้า  
            
            **การขยายพันธุ์** : ขยายพันธุ์โดยการแยกกอ ปักชำ หรือเพาะเลี้ยงเนื้อเยื่อ ''')


    elif selected_option == "กล้วยไม้สิงโตพัดแดง":
        st.image("สิงโตพัดแดง.jpg", caption="ตัวอย่างรูปภาพกล้วยไม้รสิงโตพัดแดง", use_column_width=True)
        st.success('''
            **กล้วยไม้สายพันธุ์สิงโตพัดแดง** 

            **ชื่อวิทยาศาสตร์** : Bulbophyllum flabellum-veneris  
            
            **สกุล** : สิงโตกลอกตา (Bulbophyllum) 
            
            **ลักษณะทางพฤกษศาสตร์** : มีลำลูกกล้วยขนาดเล็ก รูปไข่ยอดแหลมซึ่งเกิดระหว่าง
            ไหลช่วงระยะห่าง 0.5-1 ซม.ขนาดลำลูกกล้วย มีความสูงประมาณ 1.5 ซม. กว้างประมาณ 1.3 ซม.
            มีใบเดี่ยวยาวรีกว้าง 2-3 ซม.ใบยาวประมาณ 9-13 ซม. ก้านดอกเล็กเรียวยาว 7-14 ซม.
            ก้านดอกสีม่วงอมแดง เกิดจากตาดอกที่โคนลำลูกกล้วย มีดอกขนาดเล็ก สีตั้งแต่ม่วงแดงอ่อนๆไปจนถึงสีเข้มจัด
            มีดอกในช่อ จำนวน 12  ดอก 
            
            **วิธีการปลูก** : วัสดุที่เก็บความชื้นได้ดี โปร่ง ระบายน้ำและอากาศดี เช่น ถ่านทุบ อิฐมอญทุบ กาบมะพร้าว
            รากเฟินชายผ้าสีดา เศษกระถางแตก หินภูเขาไฟ เป็นต้น 
            
            **การรดนํ้า** : รดปานกลาง ไม่เยอะและไม่น้อยจนเกินไป 
            
            **แสงแดด** : รำไร หรือได้รับแสงในช่วงเช้า  
            
            **การขยายพันธุ์** : ขยายพันธุ์โดยการแยกกอ ปักชำ หรือเพาะเลี้ยงเนื้อเยื่อ ''')








