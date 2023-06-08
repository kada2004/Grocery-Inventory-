from tkinter import*
import pandas as pd
root=Tk()
root.title("GROCERY INVENTORY")
root.geometry("700x500")

main_label1=Label(root,text="Home Page")    
main_label1.grid(row=1,column=0,)

main_label2=Label(root,text="Item_1")    
main_label2.grid(row=2,column=0)

entry1=Entry(root)
entry1.grid(row=2,column=1)

main_label3=Label(root,text="Quantity_1")    
main_label3.grid(row=2,column=2)

entry2=Entry(root)
entry2.grid(row=2,column=3)

main_label4=Label(root,text="Price_1")    
main_label4.grid(row=2,column=4)

entry3=Entry(root)
entry3.grid(row=2,column=5)

main_label5=Label(root,text="Item_2")    
main_label5.grid(row=3,column=0)

entry4=Entry(root)
entry4.grid(row=3,column=1)

main_label6=Label(root,text="Quantity_2")    
main_label6.grid(row=3,column=2)

entry5=Entry(root)
entry5.grid(row=3,column=3)

main_label5=Label(root,text="Price_2")    
main_label5.grid(row=3,column=4)

entry6=Entry(root)
entry6.grid(row=3,column=5)

main_label6=Label(root,text="Item_3")    
main_label6.grid(row=4,column=0)

entry7=Entry(root)
entry7.grid(row=4,column=1)

main_label7=Label(root,text="Quantity_3")    
main_label7.grid(row=4,column=2)

entry8=Entry(root)
entry8.grid(row=4,column=3)

main_label7=Label(root,text="Price_3")    
main_label7.grid(row=4,column=4)

entry9=Entry(root)
entry9.grid(row=4,column=5)

main_label8=Label(root,text="Item_4")    
main_label8.grid(row=5,column=0)

entry10=Entry(root)
entry10.grid(row=5,column=1)

main_label9=Label(root,text="Quantity_4")    
main_label9.grid(row=5,column=2)

entry11=Entry(root)
entry11.grid(row=5,column=3)

main_label9=Label(root,text="Price_4")    
main_label9.grid(row=5,column=4)

entry12=Entry(root)
entry12.grid(row=5,column=5)

main_label10=Label(root,text="Item_5")    
main_label10.grid(row=6,column=0)

entry13=Entry(root)
entry13.grid(row=6,column=1)

main_label10=Label(root,text="Quantity_5")    
main_label10.grid(row=6,column=2)

entry14=Entry(root)
entry14.grid(row=6,column=3)

main_label11=Label(root,text="Price_5")    
main_label11.grid(row=6,column=4)

entry15=Entry(root)
entry15.grid(row=6,column=5)



def save_button():
    path="C:\\Users\\DAN KALENGA\\OneDrive\\Bureau\\Python Advanced\\Biendronka DB.xlsx"
    input_item_1=entry1.get()
    input_quantity_1=entry2.get()
    input_price_1=entry3.get()

    input_item_2=entry4.get()
    input_quantity_2=entry5.get()
    input_price_2=entry6.get()

    input_item_3=entry7.get()
    input_quantity_3=entry8.get()
    input_price_3=entry9.get()

    input_item_4=entry10.get()
    input_quantity_4=entry11.get()
    input_price_4=entry12.get()

    input_item_5=entry13.get()
    input_quantity_5=entry14.get()
    input_price_5=entry15.get()

    item_list=[input_item_1,input_item_2,input_item_3,input_item_4,input_item_5]
    quantity_list=[input_quantity_1,input_quantity_2,input_quantity_3,input_quantity_4,input_quantity_5]
    price_list=[input_price_1,input_price_2,input_price_3,input_price_4,input_price_5]



    data={'Item':item_list,'Quantity':quantity_list,'Price':price_list}

    index_list=[1,2,3,4,5]

    df=pd.DataFrame(data,index_list)

    df.to_excel(path)
    
    entries=[]
    for x in range(1,16):
        value="entry"+ str(x)
        entries.append(value)

    for data in entries :
        entry = eval(data)
        entry.delete(0, 'end')

    string_value=''' Data is saved 
    Item_1: {0}      Quantity_1: {1}        Price_1: {2}
    Item_2: {3}      Quantity_2: {4}        Price_2: {5}
    Item_3: {6}      Quantity_3: {7}        Price_3: {8}
    Item_4: {9}      Quantity_4: {10}       Price_4: {11}
    Item_5: {12}     Quantity_5: {13}       Price_5: {14}'''


    string_data=string_value.format(item_list[0],quantity_list[0],price_list[0],item_list[1],quantity_list[1],price_list[1],item_list[2],quantity_list[2],price_list[2],item_list[3],quantity_list[3],price_list[3],item_list[4],quantity_list[4],price_list[4])
    




    text_box.insert(END,string_data)

  
    
main_label_textbox1=Label(root,text="Output : ")    
main_label_textbox1.grid(row=9,column=0)

text_box=Text(root,width=70,height=8)
text_box.grid(row=9,column=1,columnspan=4)






button=Button(root,text="SAVE",command=save_button,pady=30,padx=45)
button.grid(row=7,column=2)

def default_Value():
   


    entries_2=[]
    for x in range(1,16):
        value="entry"+ str(x)
        entries_2.append(value)

    entries_3=["a1","a2","a3","b1","b2","b3","c1","c2","c3","d1","d2","d3","e1","e2","e3"]

    for a,b in enumerate(entries_2):
        value2=eval(b)
        value2.insert(0,entries_3[a])


    
default_button=Button(root,text="Default Value",command=default_Value,pady=30,padx=35)
default_button.grid(row=7,column=3)





root.mainloop()