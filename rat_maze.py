import time
import os
import random


statistik = {
    "jumlah_backtrack": 0,
    "log_lokasi": []
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_maze(maze, curr_x=-1, curr_y=-1, is_buntu=False):
    clear_screen()
    print("Visualisasi Rat in a Maze - Algoritma Backtracking\n")
    print("Tikus Hitam: Menunjukkan posisi terkini tikus.")
    print("Tikus Putih: Menunjukkan lintasan yang telah dilalui tikus.\n")
    
    n = len(maze)
    print("🧱" * (n + 2))
    for i in range(n):
        baris = ""
        if i == 0:
            baris += "  "  
        else:
            baris += "🧱"
            
        for j in range(n):
            if maze[i][j] == 1:
                baris += ". "
            elif maze[i][j] == 0:
                baris += "🌳"
            elif maze[i][j] == 2:
                if i == curr_x and j == curr_y:
                
                    if is_buntu:
                        baris += "❌"
                    else:
                        baris += "🐀"
                else:
                    baris += "🐁"
                    
        if i == n - 1:
            baris += "  "  
        else:
            baris += "🧱"
        print(baris)
        
    print("🧱" * (n + 2))
    
    
    if statistik["log_lokasi"]:
        print("\nLog Backtrack Terakhir:")
        for log in statistik["log_lokasi"][-5:]:
            print(log)
            
    print("\n")
    
    if is_buntu:
        time.sleep(0.4)
    else:
        time.sleep(0.2)

def is_safe(maze, x, y, n):
    if x >= 0 and x < n and y >= 0 and y < n and maze[x][y] == 1:
        return True
    return False

def solve_maze_util(maze, x, y, n):
    if x == n - 1 and y == n - 1 and maze[x][y] == 1:
        maze[x][y] = 2
        print_maze(maze, x, y)
        return True

    if is_safe(maze, x, y, n):
        maze[x][y] = 2
        print_maze(maze, x, y) 

        if solve_maze_util(maze, x + 1, y, n): return True
        if solve_maze_util(maze, x, y + 1, n): return True
        if solve_maze_util(maze, x - 1, y, n): return True
        if solve_maze_util(maze, x, y - 1, n): return True

        
        statistik["jumlah_backtrack"] += 1
        pesan_log = f"-> Mundur dari jalan buntu di Baris {x}, Kolom {y}"
        statistik["log_lokasi"].append(pesan_log)
        
        
        print_maze(maze, x, y, is_buntu=True) 
        
        maze[x][y] = 1
        return False

    return False

def generate_random_maze(n, probabilitas_tembok=0.25):
    maze = []
    for i in range(n):
        row = []
        for j in range(n):
            if (i == 0 and j == 0) or (i == n - 1 and j == n - 1):
                row.append(1)
            else:
                if random.random() < probabilitas_tembok:
                    row.append(0)
                else:
                    row.append(1)
        maze.append(row)
    return maze

def solve_maze(maze):
    n = len(maze)
    print_maze(maze) 
    time.sleep(1.5) 
    
    if not solve_maze_util(maze, 0, 0, n):
        print("Gagal: Tidak ada jalan keluar (Buntu Total)!")
        print(f"Total kemunduran (backtrack) yang dilakukan: {statistik['jumlah_backtrack']} kali.")
        return False
    
    print("\nBerhasil: Tikus menemukan jalan keluar!")
    print(f"Total kemunduran (backtrack) yang dilakukan: {statistik['jumlah_backtrack']} kali.")
    return True

if __name__ == "__main__":
    ukuran_grid = 12
    labirin_acak = generate_random_maze(ukuran_grid, probabilitas_tembok=0.25)
    solve_maze(labirin_acak)
