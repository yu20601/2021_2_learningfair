from tkinter import *
from tkinter import messagebox

### 기본 창
win=Tk()
win.title("아이스크림 할인점")
win.geometry("750x800")

py_img=[PhotoImage(file="1.png"),
        PhotoImage(file="2.png"),
        PhotoImage(file="3.png"),
        PhotoImage(file="4.png")]

label=Label(win, image=py_img[0])
label.pack()


### 창 2

def NUM2():
    global NUM1
    global NUM2
    global NUM3
    global delete_1
    global delete_all

    label.config(image=py_img[1])

    #계산하기    
    def plus_money():
        ice11 = str( ice1ent.get())
        ice22 = str( ice2ent.get())
        ice33 = str( ice3ent.get())
        ice44 = str( ice4ent.get())
        if ice11 == '' or ice22 == '' or ice33 =='' or ice44 == '':
            messagebox.showinfo("알림","0개 이상 입력해주세요.")

        else:
            

            ice1 = int(ice1ent.get())
            ice2 = int(ice2ent.get())
            ice3 = int(ice3ent.get())
            ice4 = int(ice4ent.get())
            ice1cost = ice1 * 700
            ice2cost = ice2 * 1200
            ice3cost = ice3 * 1000
            ice4cost = ice4 * 500
            total = ice1cost + ice2cost + ice3cost + ice4cost
            ice1cost_11 = str(ice1cost)
            ice2cost_22 = str(ice2cost)
            ice3cost_33 = str(ice3cost)
            ice4cost_44 = str(ice4cost)
            total_str = str(total)
            
            
        
            if ice1 < 0 or ice2 <0 or ice3 < 0 or ice4 < 0 :
                
                messagebox.showinfo("알림","0개 이상 입력해주세요.")
            
            else:
                    cost1lab["text"] = ice1cost_11 + "원"
                    cost2lab["text"] = ice2cost_22 + "원"
                    cost3lab["text"] = ice3cost_33 + "원"
                    cost4lab["text"] = ice4cost_44 + "원"
                    sumlab["text"] = total_str + "원"
                
            
    
    #라벨,버튼 삭제
    def delete_all():
        ice11 = str( ice1ent.get())
        ice22 = str( ice2ent.get())
        ice33 = str( ice3ent.get())
        ice44 = str( ice4ent.get())
        if ice11 == '' or ice22 == '' or ice33 =='' or ice44 == '' :
            messagebox.showinfo("알림","0개 이상 입력해주세요.")
        else:
            ice1lab.destroy()
            ice2lab.destroy()
            ice3lab.destroy()
            ice4lab.destroy()
                   
            cost1lab.destroy()
            cost2lab.destroy()
            cost3lab.destroy()
            cost4lab.destroy()
            sumlab.destroy()

            arrow1lab.destroy()
            arrow2lab.destroy()
            arrow3lab.destroy()
            arrow4lab.destroy()
                

            ice1ent.destroy()
            ice2ent.destroy()
            ice3ent.destroy()
            ice4ent.destroy()

            plusbtn.destroy()
            delbtn.destroy()

            
            

            ## 삭제 3 => 창 4     
            def NUM3():
                def exit_ima2():
                    exit()
            
                but_3=Button(win,text="나가기",command=exit_ima2)
                but_3.place(x=350,y=600)

                label.config(image=py_img[3])
            
            ## 삭제 2 => 창 3
            def delete_all2():
                cash_btn.destroy()
                card_btn.destroy()
                paylab.destroy()
                NUM3()
                
            cash_btn = Button(text="현금",command=delete_all2)
            cash_btn.place(x=380, y=750)


            card_btn = Button(text="카드",command=delete_all2)
            card_btn.place(x=300, y=750)

            paylab = Label(win)
            paylab.config(text = "결제수단을 선택해주세요. ")
            paylab.place(x=300, y=600)

            label.config(image=py_img[2])

            

           
            
           


    #빠삐코 라벨
    ice1lab = Label(win)
    ice1lab.config(text = "빠삐코(700원) :")
    ice1lab.place(x=200, y=550)

    arrow1lab = Label(win)
    arrow1lab.config(text = "=> ")
    arrow1lab.place(x=350, y=550)

    cost1lab= Label(win)
    cost1lab.config(text = " ")
    cost1lab.place(x=400, y=550)


    #빠삐코 입력창
    ice1ent = Entry(width=5)
    ice1ent.place(x=310, y=550)

    #브라보콘 라벨
    ice2lab = Label(win)
    ice2lab.config(text = "브라보콘(1200원) :")
    ice2lab.place(x=200, y=600)

    arrow2lab = Label(win)
    arrow2lab.config(text = "=> ")
    arrow2lab.place(x=350, y=600)

    cost2lab = Label(win)
    cost2lab.config(text = " ")
    cost2lab.place(x=400, y=600)

    #브라보콘 입력창
    ice2ent = Entry(width=5)
    ice2ent.place(x=310, y=600)

    #죠스바 라벨
    ice3lab = Label(win)
    ice3lab.config(text = "죠스바(1000원) :")
    ice3lab.place(x=200, y=650)

    arrow3lab = Label(win)
    arrow3lab.config(text = "=> ")
    arrow3lab.place(x=350, y=650)

    cost3lab = Label(win)
    cost3lab.config(text = " ")
    cost3lab.place(x=400, y=650)

    #죠스바 입력창
    ice3ent = Entry(width=5)
    ice3ent.place(x=310, y=650)

    #바밤바 라벨
    ice4lab = Label(win)
    ice4lab.config(text = "바밤바(500원):")
    ice4lab.place(x=200, y=700)

    arrow4lab = Label(win)
    arrow4lab.config(text = "=> ")
    arrow4lab.place(x=350, y=700)

    cost4lab = Label(win)
    cost4lab.config(text = " ")
    cost4lab.place(x=400, y=700)


    #바밤바 입력창
    ice4ent = Entry(width=5)
    ice4ent.place(x=310, y=700)



    #합계산 버튼
    plusbtn = Button(text="합 계산", command=plus_money)
    plusbtn.place(x=270, y=750)

    sumlab = Label(win)
    sumlab.config(text = " ")
    sumlab.place(x=400, y=750)

    #삭제 버튼
    delbtn = Button(text="다음", command=delete_all)
    delbtn.place(x=480, y=750)


def NUM1():
    global NUM1
    global NUM2
    global NUM3
    global delete_1
    global delete_all


    
    ### 창 1
    
    def delete_1():
        but_1.destroy()
        but_2.destroy()
        NUM2()


    def exit_ima():
        exit()

    but_1=Button(win,text="아이스크림 구매하기",command=delete_1)
    but_1.place(x=150,y=600)

    but_2=Button(win,text="나가기",command=exit_ima)
    but_2.place(x=500,y=600)

NUM1()


win.mainloop()






