import tkinter
import tkinter.messagebox
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


key = 0 # 키 이름을 입력할 변수 선언
mx = 1 # 캐릭터의 가로 뱡향 위치를 관리하는 변수
my = 1 # 캐릭터의 세로 뱡향 위치를 관리하는 변수
yuka = 0 # 칠해진 칸을 세는 변수

# 키를 눌렀을 때 실행할 함수 정의
def key_down(e):
    global key # key을 전역 변수로 취급
    key = e.keysym # 눌려진 키 이름을 key에 대입

    
# 키를 눌렀다 뗐을 때 실행할 함수 정의
def key_up(e):
    global key # key을 전역 변수로 취급
    key = "" # key에 빈 문자열 대입

    
# 게임 초기화 함수
def reset():
    global mx, my, yuka
    canvas.delete("PAINT")
    mx = 1
    my = 1
    yuka = 0
    for y in range(7):
        for x in range(10):
            if maze[y][x] == 2:
                maze[y][x] = 0

                
# 실시간 처리를 수행할 함수 정의
def main_proc():
    global mx, my, yuka # mx, my, yuka를 전역 변수로 선언
        
    # Esc 키를 누를 시 게임 종료
    if key == "Escape":
        root.destroy()
        return ;
        
    # 왼쪽 Shift 키를 눌렀고 미로가 2칸 이상 칠해진 상태라면 게임 초기화
    if key == "Shift_L" and yuka > 1:
        reset()
                        
    # key 방향이 통로라면 그 방향에 맞게 mx, my값을 변경
    if key == "Up" and maze[my-1][mx] == 0: 
        my -= 1
    if key == "Down" and maze[my+1][mx] == 0:
        my += 1
    if key == "Left" and maze[my][mx-1] == 0:
        mx -= 1
    if key == "Right" and maze[my][mx+1] == 0:
        mx += 1    
    
    # 캐릭터가 있는 장소가 벽이 아니라면 리스트 값을 2로 변경,
    # 칠한 회수를 1 증가시키고, 해당 위치를 분홍색으로 칠한다.
    if maze[my][mx] == 0:
        maze[my][mx] = 2
        yuka += 1
        # PAINT(지났던 길) 태그 추가
        canvas.create_rectangle(mx*80, my*80, mx*80 + 79, my*80 + 79, 
                                   fill="pink", width=0, tag="PAINT")
    canvas.delete("MYCHR")
    canvas.create_image(mx*80 + 40, my*80 + 40, image=img, tag="MYCHR") # 캐릭터 이미지 이동
    
    # 30개 칸을 모두 칠했다면 클리어 메시지를 표시해준 후에 게임 초기화
    if yuka == 30:
        canvas.update()
        tkinter.messagebox.showinfo("축하합니다!", "모든 바닥을 칠했습니다!")
        reset()
    # 사방이 전부 막혀 이동할 수 없어서 클리어 할 수 없는 상황일 때 
    # 클리어 불가능 메시지를 표시해준 후에 게임 초기화
    elif 0 not in [maze[my-1][mx], maze[my+1][mx], maze[my][mx-1], maze[my][mx+1]]:
        tkinter.messagebox.showinfo("망했어요!", "클리어가 불가능합니다\n다시 시작하세요!")
        reset()
    
    # 0.1초 후 main_proc 함수를 실행
    root.after(100, main_proc)
                            

root = tkinter.Tk()
root.title("미로를 칠하는 중")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=800, height=560, bg="white")
canvas.pack()

# 미로 생성
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            canvas.create_rectangle(x * 80, y * 80, x * 80 + 79, y * 80 + 79, fill="skyblue", width=0)

img = tkinter.PhotoImage(file=resource_path("mimi_s.png"))
# MYCHR(캐릭터) 태그 추가
canvas.create_image(mx * 80 + 40, my * 80 + 40, image=img, tag="MYCHR")
main_proc()
root.mainloop()