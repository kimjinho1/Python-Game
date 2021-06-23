import tkinter
import random
# from functools import partial
from PIL import ImageTk
import os


# PyInstaller에 의해 임시폴더에서 실행될 경우 임시폴더로 접근하는 함수
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def click_btn(user_choice):
    # 가위, 바위, 보 중 랜덤으로 하나 선택하고 com_rps_label에 출력
    computer_choice = random.choice(["가위", "바위", "보"])
    com_rps_label["text"] = computer_choice
    com_rps_label.update()
    
    # 사용자가 선택한 것을 user_rps_label에 출력
    user_rps_label["text"] = user_choice
    user_rps_label.update()
    
    # 승패를 판별하고 result_label에 출력
    res = ""
    if computer_choice == user_choice:
        res = "비김!" 
    else:
        if user_choice == "가위":
            res = "승리!" if computer_choice == "보" else "패배!"
        elif user_choice == "바위":
            res = "승리!" if computer_choice == "가위" else "패배!"
        elif user_choice == "보":
            res = "승리!" if computer_choice == "바위" else "패배!"
    result_label["text"] = res
    result_label.update()
    
if __name__ == "__main__":
    root = tkinter.Tk() 
    root.title("가위바위보 프로그램")
    root.resizable(False, False) 
    canvas = tkinter.Canvas(root, width=800, height=480)
    canvas.pack()

    # 이미지 파일에 따라 tkinter.PhotoImage가 잘 작동하지 않는 것 같다.
    # ImageTk.PhotoImage 명령을 대신 사용했다.
    # gazou = tkinter.PhotoImage(file="alphago.png")
    gazou = ImageTk.PhotoImage(file=resource_path("alphago.png"))
    canvas.create_image(400, 240, image=gazou)
    
    # 컴퓨터, 사용자 라벨
    com_label = tkinter.Label(root, text="컴퓨터", font=("Times New Roman", 55),
                            bg="white")
    user_label = tkinter.Label(root, text="사용자", font=("Times New Roman", 55),
                            bg="white")
    # 컴퓨터 가위, 바위, 보 라벨
    com_rps_label = tkinter.Label(root, text="??", font=("Times New Roman", 55),
                            bg="white")
    # 사용자 가위, 바위, 보 라벨
    user_rps_label = tkinter.Label(root, text="??", font=("Times New Roman", 55),
                            bg="white")
    # 승패 결과 라벨
    result_label = tkinter.Label(root, text="승패", font=("Times New Roman", 60),
                            bg="white")
    com_label.place(x=350, y=25)
    com_rps_label.place(x=600, y=25)
    user_label.place(x=350, y=145)
    user_rps_label.place(x=600, y=145)
    result_label.place(x=470, y=250)

    # 가위, 바위, 보 버튼 3개
    # 버튼 명령에 인수를 전달하기 위해 lambda를 사용했다.
    # partial(clict_btn, "가위") 같은 방식으로도 사용할 수 있다.
    s_button = tkinter.Button(root, text="가위", font=("Times New Roman", 36),
                            fg="skyblue", command=lambda: click_btn("가위"))
    r_button = tkinter.Button(root, text="바위", font=("Times New Roman", 36),
                            fg="skyblue", command=lambda: click_btn("바위"))
    p_button = tkinter.Button(root, text="보", font=("Times New Roman", 36),
                            fg="skyblue", command=lambda: click_btn("보"))
    s_button.place(x=350, y=365)
    r_button.place(x=520, y=365)
    p_button.place(x=690, y=365)

    root.mainloop() 