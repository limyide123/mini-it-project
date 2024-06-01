import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import font
from tkinter import *
from ttkbootstrap import Style
from PIL import Image, ImageTk
from ttkbootstrap.scrolled import ScrolledFrame
import os
from tkinter import PhotoImage
import sqlite3
from tkinter import Tk, filedialog

def setup_database():
    conn = sqlite3.connect('clash_royale.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        directory TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER,
        filename TEXT,
        FOREIGN KEY (category_id) REFERENCES categories (id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS profilecards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        rarity TEXT,
        elixir INTEGER,
        card_type TEXT,
        arena TEXT,
        description TEXT,
        hitpoints INTEGER,
        damage INTEGER,
        card_range INTEGER,
        stun_duration REAL,
        shield TEXT,
        movement_speed TEXT,
        radius REAL,
        image_path TEXT
    )
    ''')

    categories = [
        ('Common', 'common'),
        ('Rare', 'rare'),
        ('Epic', 'epic'),
        ('Legendary', 'legendary'),
        ('Champion', 'champion'),
        ('Funny', 'funny'),
        ('Elixir_1', 'elixir_1'),
        ('Elixir_2', 'elixir_2'),
        ('Elixir_3', 'elixir_3'),
        ('Elixir_4', 'elixir_4'),
        ('Elixir_5', 'elixir_5'),
        ('Elixir_6', 'elixir_6'),
        ('Elixir_7', 'elixir_7'),
        ('Elixir_8', 'elixir_8'),
        ('Elixir_9', 'elixir_9'),
        ('Spells', 'spells'),
        ('Buildings', 'buildings'),
        ('Troop', 'troop'),
        ('Arena_0', 'arena_0'),
        ('Arena_1', 'arena_1'),
        ('Arena_2', 'arena_2'),
        ('Arena_3', 'arena_3'),
        ('Arena_4', 'arena_4'),
        ('Arena_5', 'arena_5'),
        ('Arena_6', 'arena_6'),
        ('Arena_7', 'arena_7'),
        ('Arena_8', 'arena_8'),
        ('Arena_9', 'arena_9'),
        ('Arena_10', 'arena_10'),
        ('Arena_11', 'arena_11'),
        ('Arena_12', 'arena_12'),
        ('Arena_13', 'arena_13'),
        ('Arena_14', 'arena_14'),
        ('Arena_15', 'arena_15'),
        ('Arena_16', 'arena_16'),
        ('Arena_17', 'arena_17'),
        ('Arena_18', 'arena_18'),
    ]

    for category_name, directory in categories:
        cursor.execute('SELECT id FROM categories WHERE name = ?', (category_name,))
        category_id = cursor.fetchone()
        if not category_id:
            cursor.execute('INSERT INTO categories (name, directory) VALUES (?, ?)', (category_name, directory))
            category_id = cursor.lastrowid
        else:
            category_id = category_id[0]

        image_dir = os.path.join("clash-royale-card-elixir", directory)
        for filename in os.listdir(image_dir):
            if filename.endswith('.png'):
                cursor.execute('SELECT id FROM images WHERE category_id = ? AND filename = ?', (category_id, filename))
                if not cursor.fetchone():
                    cursor.execute('INSERT INTO images (category_id, filename) VALUES (?, ?)', (category_id, filename))

    conn.commit()
    conn.close()



window = ttk.Window(themename='solar')
window.title("ClashPedia")

top_frame = tk.Frame(window, bg='#c3c3c3')
top_frame.pack(side=tk.TOP)
top_frame.pack_propagate(False)
top_frame.configure(height='150' , width='1925')

lb = tk.Label(top_frame , text= 'ClashPedia (Clash Royale Encyclopedia)', font=('Showcard Gothic', 36, 'bold'))
lb.place(x=20 , y = 10)
lb.pack(padx=10 ,pady=20)

options_frame = tk.Frame(window, bg='#c3c3c3')
options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(height='800' , width='175')

main_frame = tk.Frame(window)
main_frame.pack(side=LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height='1000' ,width='1750')

logo_dir = "design_photo"
logo_filename = "logo.png"
logo_path = os.path.join(logo_dir, logo_filename)

logo_img = Image.open(logo_path)
logo_img = logo_img.resize((160, 150), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_img)

logo_label = tk.Label(top_frame, image=logo_photo, bg='#c3c3c3')
logo_label.place(x=10, y=20)  

def hide_switch_page():
    welcome_switch_page.config(bg='#c3c3c3')
    categories_switch_page.config(bg='#c3c3c3')
    deck_builder_switch_page.config(bg='#c3c3c3')
    profile_maker_switch_page.config(bg='#c3c3c3')


def delete_page():
    for frame in main_frame.winfo_children():
        frame.destroy()


def switch_page(lb ,page):
    hide_switch_page()
    lb.configure(bg='#158aff')
    delete_page()
    page()


def welcome_page():
    welcome_frame = ScrolledFrame(main_frame, padding=5, height=10, autohide=True)
    welcome_frame.pack(fill=BOTH, expand=YES)

    text_label = tk.Label(welcome_frame, text='Welcome to ClashPedia, your ultimate guide to Clash Royale!\nExplore cards, strategies, updates, and much more.', font=('Showcard Gothic', 23, 'bold'))
    text_label.pack(pady=10)

    banner_path = "design_photo/banner.png"
    image = Image.open(banner_path)
    image = ImageTk.PhotoImage(image)

    image_label = tk.Label(welcome_frame, image=image)
    image_label.image = image
    image_label.pack()

    tutorial_of_cards_label = tk.Label(welcome_frame, text='What is "CLASH ROYALE?"', font=('Rockwell Extra Bold', 15, 'bold'))
    tutorial_of_cards_label.pack(pady=10, anchor='w', padx=20)

    tutorial_of_cards_text = """
    Winning Battles:
    - Get more Crowns than your opponent by destroying their Crown Towers.
    - Destroying the opponent's King's Tower instantly gives you 3 Crowns and wins the game.
    - If no King's Tower is destroyed, the player with more Crowns at the end of the 3-minute period wins.
    - If neither player has more Crowns, the game goes into Overtime.
    - Overtime ends if a Crown Tower is destroyed, deciding the winner.
    - If all towers have identical health, a tiebreaker occurs where towers rapidly lose health until one is destroyed.

    Trophies and Rewards:
    - Winning earns Trophies, while losing loses them.
    - Trophies unlock new Arenas and higher Leagues.
    - New Arenas offer new Cards and better rewards.
    - Victory in Challenges and Tournaments earns rewards and progresses in the event.

    Clan Wars:
    - In a stalemate, a coin flip decides the winner.
    - Trophies contribute to Clan War standings and rewards.1. Troops: These are units that can move and attack.
        2. Spells: These are temporary effects that can be cast anywhere on the battlefield.
        3. Buildings: These are stationary structures that decay over time.
        4. Tower Troops: These are troops that stay on your Crown Towers and attack enemy troops.
    """
    tutorial_of_cards_info = tk.Label(welcome_frame, text=tutorial_of_cards_text, justify='left')
    tutorial_of_cards_info.pack(pady=5, anchor='w', padx=40)  

    types_frame = tk.Frame(welcome_frame, bg="white", bd=2, relief=tk.GROOVE)
    types_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    tutorial_of_cards_label = tk.Label(types_frame, text='Types of Cards:', font=('Rockwell Extra Bold', 15, 'bold'))
    tutorial_of_cards_label.pack(pady=10, anchor='w', padx=20)

    tutorial_of_cards_text = """
    1. Troops: These are units that can move and attack.
    2. Spells: These are temporary effects that can be cast anywhere on the battlefield.
    3. Buildings: These are stationary structures that decay over time.
    4. Tower Troops: These are troops that stay on your Crown Towers and attack enemy troops.
    """
    tutorial_of_cards_info = tk.Label(types_frame, text=tutorial_of_cards_text, justify='left')
    tutorial_of_cards_info.pack(pady=5, anchor='w', padx=40)

    rarities_frame = tk.Frame(welcome_frame, bg="white", bd=2, relief=tk.GROOVE)
    rarities_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    rarities_and_levels_label = tk.Label(rarities_frame, text='Rarities and Levels:', font=('Rockwell Extra Bold', 15, 'bold'))
    rarities_and_levels_label.pack(pady=10, anchor='w', padx=20)

    rarities_and_levels_text = """
    - Common: Levels 1 to 15
    - Rare: Levels 3 to 15
    - Epic: Levels 6 to 15
    - Legendary: Levels 9 to 15
    - Champion: Levels 11 to 15
    """
    rarities_and_levels_info = tk.Label(rarities_frame, text=rarities_and_levels_text, justify='left')
    rarities_and_levels_info.pack(pady=5, anchor='w', padx=40)

    champion_frame = tk.Frame(welcome_frame, bg="white", bd=2, relief=tk.GROOVE)
    champion_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    champion_cards_label = tk.Label(champion_frame, text='Champion Cards:', font=('Rockwell Extra Bold', 15, 'bold'))
    champion_cards_label.pack(pady=10, anchor='w', padx=20)

    champion_cards_text = """
    - Unique troops with special abilities.
    - Can be activated by tapping an icon on the screen, costing Elixir.
    - Abilities have a cooldown after use.
    - Not affected by regular card cycle rules.
    - Only one Champion card allowed in a deck.
    - Mirror cannot spawn Champions.
    - Cloned Champions can't use abilities.
    """
    champion_cards_info = tk.Label(champion_frame, text=champion_cards_text, justify='left')
    champion_cards_info.pack(pady=5, anchor='w', padx=40)

    ranges_frame = tk.Frame(welcome_frame, bg="white", bd=2, relief=tk.GROOVE)
    ranges_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    ranges_label = tk.Label(ranges_frame, text='Ranges:', font=('Rockwell Extra Bold', 15, 'bold'))
    ranges_label.pack(pady=10, anchor='w', padx=20)

    ranges_text = """
    - Melee: Short (0.8 tiles or less)
    - Melee: Medium (1.2 tiles)
    - Melee: Long (1.6 tiles)
    - Ranged (2 or more tiles)
    """
    ranges_info = tk.Label(ranges_frame, text=ranges_text, justify='left')
    ranges_info.pack(pady=5, anchor='w', padx=40)

    welcome_frame.pack()
    
def categories_page(category=None):
    def clear_main_frame():
        for widget in main_frame.winfo_children():
            widget.destroy()

    def show_categories(category):
        clear_main_frame()

        categories = {
            'type': ["Spells", "Troop", "Buildings"],
            'arena': ["Arena_0", "Arena_1", "Arena_2", "Arena_3", "Arena_4", "Arena_5", "Arena_6", "Arena_7", "Arena_8", "Arena_9", "Arena_10", "Arena_11", "Arena_12", "Arena_13", "Arena_14", "Arena_15", "Arena_16", "Arena_17", "Arena_18"],
            'elixir': ["Elixir_1", "Elixir_2", "Elixir_3","Elixir_4","Elixir_5","Elixir_6","Elixir_7","Elixir_8","Elixir_9"],
            'rarity': ["Common", "Rare", "Epic", "Legendary", "Champion", "Funny"]
        }


        title_label = tk.Label(main_frame, text=category.capitalize(), font=('Showcard Gothic', 25, 'bold'))
        title_label.pack(pady=10)

        button_frame = tk.Frame(main_frame)
        button_frame.pack(fill=X, padx=10, pady=5)

        type_button = ttk.Button(button_frame, text='Type', command=lambda: show_categories('type'))
        type_button.pack(side=LEFT, padx=5)

        arena_button = ttk.Button(button_frame, text='Arena', command=lambda: show_categories('arena'))
        arena_button.pack(side=LEFT, padx=5)

        elixir_button = ttk.Button(button_frame, text='Elixir', command=lambda: show_categories('elixir'))
        elixir_button.pack(side=LEFT, padx=5)

        rarity_button = ttk.Button(button_frame, text='Rarity', command=lambda: show_categories('rarity'))
        rarity_button.pack(side=LEFT, padx=5)

        category_frame = ScrolledFrame(main_frame, autohide=True)
        category_frame.pack(fill=BOTH, expand=YES, padx=10, pady=10)

        row = 0
        for title in categories.get(category, []):


            title_label = tk.Label(category_frame, text=title, font=('Showcard Gothic', 16, 'bold'))
            title_label.pack(pady=5)

            img_dir = os.path.join("clash-royale-card-elixir", title)
            if os.path.isdir(img_dir):
                image_count = 0
                img_frame = tk.Frame(category_frame)
                img_frame.pack()
                for filename in os.listdir(img_dir):
                    if filename.endswith('.png'):
                        img_path = os.path.join(img_dir, filename)
                        img = Image.open(img_path)
                        img = img.resize((90, 120), Image.LANCZOS)
                        img = ImageTk.PhotoImage(img)

                        panel = tk.Label(img_frame, image=img, compound=tk.LEFT, bd=0, padx=5, pady=5)
                        panel.image = img
                        panel.grid(row=image_count // 13, column=image_count % 13)
                        image_count += 1

                        panel.bind("<Button-1>", lambda event, img_path=img_path: show_image(event, img_path))

    clear_main_frame()

    button_frame = tk.Frame(main_frame)
    button_frame.pack(fill=X, padx=10, pady=5)

    type_button = ttk.Button(button_frame, text='Type', command=lambda: show_categories('type'))
    type_button.pack(side=LEFT, padx=5)

    arena_button = ttk.Button(button_frame, text='Arena', command=lambda: show_categories('arena'))
    arena_button.pack(side=LEFT, padx=5)

    elixir_button = ttk.Button(button_frame, text='Elixir', command=lambda: show_categories('elixir'))
    elixir_button.pack(side=LEFT, padx=5)

    rarity_button = ttk.Button(button_frame, text='Rarity', command=lambda: show_categories('rarity'))
    rarity_button.pack(side=LEFT, padx=5)

    if category:
        show_categories(category)

    else:
        show_categories('rarity')

def show_image(event, image_path):
    image_window = tk.Toplevel()
    image_window.title("Card Image")
    image_window.geometry("300x400")

    img = Image.open(image_path)
    img = img.resize((300, 400), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)

    image_label = tk.Label(image_window, image=img)
    image_label.image = img
    image_label.pack(padx=20, pady=20)

def deck_builder_page():
    deck_builder_frame = ScrolledFrame(main_frame, autohide=True)
    deck_builder_frame.pack(fill=BOTH, expand=YES, padx=10, pady=10)
    lb = tk.Label(deck_builder_frame, text='Deck Builder', font=('Showcard Gothic', 30, 'bold'))
    lb.place(x=20, y=10)
    lb.pack(padx=10, pady=20)

    categories = [("Win Condition", "WinCondition", 1, 2,), ("Spells", "Spells", 1, 3), ("Mini Tanks", "MiniTanks", 0, 2), ("Buildings", "Buildings", 0, 2), ("Damage Units", "DamageUnits", 2, 4)]

    for section, category, min_val, max_val in categories:
        category_frame = tk.Frame(deck_builder_frame)
        category_frame.pack(pady=10, padx=10, fill=tk.X)

        lb = tk.Label(category_frame, text=section, font=('Showcard Gothic', 15, 'bold'))
        lb.pack(padx=10, pady=10)
        for i in range(15):
            row_frame = tk.Frame(category_frame, bg="white")
            row_frame.pack()
            for j in range(13):
                try:
                    # Adjust the filename to parse elixir cost
                    file_name = f"card_{i*13 + j + 1}.png"
                    image_path = f"deck_builder_images/{category}/{file_name}"

                    img = Image.open(image_path)
                    img = img.resize((90, 120), Image.LANCZOS)
                    img = ImageTk.PhotoImage(img)
                    panel = tk.Label(row_frame, image=img, compound=tk.LEFT, bd=0, padx=5, pady=5)
                    panel.image = img
                    panel.pack(side=tk.LEFT)

                    var = tk.BooleanVar()
                    checkbutton = ttk.Checkbutton(row_frame, variable=var, command=lambda v=var, p=panel, min_val=min_val, max_val=max_val, cat=category, fname=file_name: on_checkbutton_click(v, p, min_val, max_val, cat, fname))
                    checkbutton.pack(side=tk.LEFT, padx=5, pady=5)

                except FileNotFoundError:
                    break

    results_btn = tk.Button(deck_builder_frame, text="Results", command=show_results)
    results_btn.pack(padx=10, pady=10)


num_selected = 0 
category_counts = {
    "WinCondition": 0,
    "Spells": 0,
    "MiniTanks": 0,
    "Buildings": 0,
    "DamageUnits": 0
}

elixir_category_counts = 0

elixir_category_counts = {"WinCondition": 0, "Spells": 0, "MiniTanks": 0, "Buildings": 0, "DamageUnits": 0}

elixir_costs = {
    "card_1.png": 2,
    "card_2.png": 3,
    "card_3.png": 3,
    "card_4.png": 3,
    "card_5.png": 3,
    "card_6.png": 4,
    "card_7.png": 4,
    "card_8.png": 4,
    "card_9.png": 4,
    "card_10.png": 5,
    "card_11.png": 5,
    "card_12.png": 5,
    "card_13.png": 5,
    "card_14.png": 5,
    "card_15.png": 6,
    "card_16.png": 6,
    "card_17.png": 6,
    "card_18.png": 7,
    "card_19.png": 7,
    "card_20.png": 8,
    "card_21.png": 9,
    "card_27.png": 1,
    "card_28.png": 2,
    "card_29.png": 2,
    "card_30.png": 2,
    "card_31.png": 2,
    "card_32.png": 2,
    "card_33.png": 3,
    "card_34.png": 3,
    "card_35.png": 3,
    "card_36.png": 3,
    "card_37.png": 3,
    "card_38.png": 4,
    "card_39.png": 4,
    "card_40.png": 4,
    "card_41.png": 6,
    "card_42.png": 6,
    "card_53.png": 2,
    "card_54.png": 3,
    "card_55.png": 3,
    "card_56.png": 3,
    "card_57.png": 3,
    "card_58.png": 4,
    "card_59.png": 4,
    "card_60.png": 4,
    "card_61.png": 4,
    "card_62.png": 4,
    "card_63.png": 4,
    "card_64.png": 4,
    "card_65.png": 4,
    "card_66.png": 4,
    "card_67.png": 4,
    "card_68.png": 5,
    "card_69.png": 5,
    "card_70.png": 5,
    "card_71.png": 5,
    "card_72.png": 5,
    "card_73.png": 6,
    "card_79.png": 3,
    "card_80.png": 3,
    "card_81.png": 4,
    "card_82.png": 4,
    "card_83.png": 4,
    "card_84.png": 4,
    "card_85.png": 5,
    "card_86.png": 5,
    "card_87.png": 6,
    "card_88.png": 7,
    "card_92.png": 1,
    "card_93.png": 1,
    "card_94.png": 1,
    "card_95.png": 1,
    "card_96.png": 1,
    "card_97.png": 2,
    "card_98.png": 2,
    "card_99.png": 2,
    "card_100.png": 2,
    "card_101.png": 3,
    "card_102.png": 3,
    "card_103.png": 3,
    "card_104.png": 3,
    "card_105.png": 3,
    "card_106.png": 3,
    "card_107.png": 3,
    "card_108.png": 3,
    "card_109.png": 3,
    "card_110.png": 3,
    "card_111.png": 3,
    "card_112.png": 4,
    "card_113.png": 4,
    "card_114.png": 4,
    "card_115.png": 4,
    "card_116.png": 4,
    "card_117.png": 4,
    "card_118.png": 4,
    "card_119.png": 4,
    "card_120.png": 4,
    "card_121.png": 4,
    "card_122.png": 4,
    "card_123.png": 5,
    "card_124.png": 5,
    "card_125.png": 5,
    "card_126.png": 5,
    "card_127.png": 5,
    "card_128.png": 5,
    "card_129.png": 6,
    "card_130.png": 6,
    "card_131.png": 7,
    "card_132.png": 7,
    "card_133.png": 7,
}

def on_checkbutton_click(var, panel, min_val, max_val, category, file_name):
    global num_selected, category_counts, elixir_category_counts
    if var.get():
        
        if num_selected >= 8:
            messagebox.showwarning("Limit Exceeded", "You can only select up to 8 cards.")
            var.set(False)
            return

        elixir_cost = elixir_costs[file_name]  # Get the elixir cost from the dictionary
        elixir_category_counts[category] += elixir_cost
        category_counts[category] += 1
        num_selected += 1
        panel.config(state='normal')
    else:
        elixir_cost = elixir_costs[file_name]  # Get the elixir cost from the dictionary
        elixir_category_counts[category] -= elixir_cost
        category_counts[category] -= 1
        num_selected -= 1
        panel.config(state='normal')

def show_results():
    if num_selected < 8:
        messagebox.showwarning("Warning", "You must select 8 cards!")
    else:
        total_elixir = sum(elixir_category_counts.values())
        average_elixir = total_elixir / 8
        results = []
        categories = [("Win Condition", "WinCondition", 1, 2), ("Spells", "Spells", 1, 3), ("Mini Tanks", "MiniTanks", 0, 2), ("Buildings", "Buildings", 0, 2), ("Damage Units", "DamageUnits", 2, 4)]

        feedback = ""
        if 0.1 <= average_elixir <= 2.0:
            feedback = "You're a fast cycle guy"
        elif 2.1 <= average_elixir <= 3.2:
            feedback = "You're either using 2.6 hog or 2.9 mortar"
        elif 3.3 <= average_elixir <= 4.1:
            feedback = "You're not dependent on cycle decks now"
        elif 4.2 <= average_elixir <= 4.7:
            feedback = "Woah, that's a bit too expensive"
        elif 4.8 <= average_elixir <= 5.6:
            feedback = "Are you trolling at this point?"
        else:
            feedback = "I'm certain you're playing 7x elixir"

        for section, category, min_val, max_val, in categories:
            if category_counts[category] < min_val or category_counts[category] > max_val:
                results.append(f"{section}: bad")
            else:
                results.append(f"{section}: good")

        messagebox.showinfo("Results", "\n".join(results) + "\n" + "\n" + "Average Elixir: {:.2f}\nFeedback: {}".format(average_elixir, feedback))

def save_card_to_file(name, rarity, elixir, card_type, arena, description, hitpoints, damage, card_range, stun_duration, shield, movement_speed, radius, image_path=None):
    if not name or not rarity or not elixir or not card_type or not arena or not description:
        messagebox.showwarning("Input Error", "Name, Rarity, Elixir, Type, Arena, and Description are required fields.")
        return

    try:
        elixir = int(elixir)
        hitpoints = int(hitpoints)
        damage = int(damage)
        card_range = int(card_range)
        stun_duration = float(stun_duration)
        radius = float(radius)
    except ValueError:
        messagebox.showwarning("Input Error", "Elixir, Hitpoints, Damage, Range, Stun Duration, and Radius must be numbers.")
        return

    conn = sqlite3.connect('clash_royale.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO profile_cards (name, raity, elixir, card_type, arena, description, hitpoints, damage, card_range, stun_duration, shield, movement_speed, radius, image_path)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, rarity, elixir, card_type, arena, description.strip(), hitpoints, damage, card_range, stun_duration, shield, movement_speed, radius, image_path))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Card saved successfully.")

def upload_image():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Select an image", filetypes=[('Image files', '*.png *.jpg *.jpeg')])
    root.destroy()  # Close the file explorer window
    return file_path


def profile_maker_page():
    profile_maker_frame = ScrolledFrame(main_frame, padding=5, height=10, autohide=True)
    profile_maker_frame.pack(fill=BOTH, expand=YES)

    title_label = tk.Label(profile_maker_frame, text="Profile Maker", font=('Showcard Gothic', 25, 'bold'))
    title_label.pack(pady=10)

    form_frame = tk.Frame(profile_maker_frame)
    form_frame.pack(pady=10, padx=10)

    name_label = tk.Label(form_frame, text="Card Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(form_frame)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    rarity_label = tk.Label(form_frame, text="Rarity:")
    rarity_label.grid(row=1, column=0, padx=5, pady=5)
    rarity_entry = tk.Entry(form_frame)
    rarity_entry.grid(row=1, column=1, padx=5, pady=5)

    elixir_label = tk.Label(form_frame, text="Elixir Cost:")
    elixir_label.grid(row=2, column=0, padx=5, pady=5)
    elixir_entry = tk.Entry(form_frame)
    elixir_entry.grid(row=2, column=1, padx=5, pady=5)

    type_label = tk.Label(form_frame, text="Card Type:")
    type_label.grid(row=3, column=0, padx=5, pady=5)
    type_entry = tk.Entry(form_frame)
    type_entry.grid(row=3, column=1, padx=5, pady=5)

    arena_label = tk.Label(form_frame, text="Arena:")
    arena_label.grid(row=4, column=0, padx=5, pady=5)
    arena_entry = tk.Entry(form_frame)
    arena_entry.grid(row=4, column=1, padx=5, pady=5)

    description_label = tk.Label(form_frame, text="Description:")
    description_label.grid(row=5, column=0, padx=5, pady=5)
    description_text = tk.Text(form_frame, height=5, width=40)
    description_text.grid(row=5, column=1, padx=5, pady=5)

    hitpoints_label = tk.Label(form_frame, text="Hitpoints:")
    hitpoints_label.grid(row=6, column=0, padx=5, pady=5)
    hitpoints_entry = tk.Entry(form_frame)
    hitpoints_entry.grid(row=6, column=1, padx=5, pady=5)

    damage_label = tk.Label(form_frame, text="Damage:")
    damage_label.grid(row=7, column=0, padx=5, pady=5)
    damage_entry = tk.Entry(form_frame)
    damage_entry.grid(row=7, column=1, padx=5, pady=5)

    range_label = tk.Label(form_frame, text="Range:")
    range_label.grid(row=8, column=0, padx=5, pady=5)
    range_entry = tk.Entry(form_frame)
    range_entry.grid(row=8, column=1, padx=5, pady=5)

    stun_duration_label = tk.Label(form_frame, text="Stun Duration:")
    stun_duration_label.grid(row=9, column=0, padx=5, pady=5)
    stun_duration_entry = tk.Entry(form_frame)
    stun_duration_entry.grid(row=9, column=1, padx=5, pady=5)

    shield_label = tk.Label(form_frame, text="Shield:")
    shield_label.grid(row=10, column=0, padx=5, pady=5)
    shield_entry = tk.Entry(form_frame)
    shield_entry.grid(row=10, column=1, padx=5, pady=5)

    movement_speed_label = tk.Label(form_frame, text="Movement Speed:")
    movement_speed_label.grid(row=11, column=0, padx=5, pady=5)
    movement_speed_entry = tk.Entry(form_frame)
    movement_speed_entry.grid(row=11, column=1, padx=5, pady=5)

    radius_label = tk.Label(form_frame, text="Radius:")
    radius_label.grid(row=12, column=0, padx=5, pady=5)
    radius_entry = tk.Entry(form_frame)
    radius_entry.grid(row=12, column=1, padx=5, pady=5)

    save_button = tk.Button(form_frame, text="Save", command=lambda: save_card_to_file(
        name_entry.get(),
        rarity_entry.get(),
        elixir_entry.get(),
        type_entry.get(),
        arena_entry.get(),
        description_text.get("1.0", tk.END),
        hitpoints_entry.get(),
        damage_entry.get(),
        range_entry.get(),
        stun_duration_entry.get(),
        shield_entry.get(),
        movement_speed_entry.get(),
        radius_entry.get()
    ))
    save_button.grid(row=13, column=0, columnspan=2, pady=10)

    upload_button = ttk.Button(form_frame, text="Upload Image", command=upload_image)
    upload_button.grid(row=14, column=1, padx=5)

    profile_maker_frame.pack()


welcome_button = ttk.Button(options_frame , text= 'Welcome' , command=lambda:switch_page(welcome_switch_page,welcome_page))
welcome_button.place(x=20 , y= 20, width=130)
welcome_switch_page = tk.Label(options_frame, text='', bg='#c3c3c3')
welcome_switch_page.place(x=3, y=20, width=5, height =40)

categories_button = ttk.Button(options_frame , text= 'Categories' , command=lambda:switch_page(categories_switch_page,categories_page))
categories_button.place(x=20 , y= 80, width=130)
categories_switch_page = tk.Label(options_frame, text='', bg='#c3c3c3')
categories_switch_page.place(x=3, y=80, width=5, height =40)

deck_builder_button = ttk.Button(options_frame , text= 'Deck Builder' , command=lambda:switch_page(deck_builder_switch_page,deck_builder_page))
deck_builder_button.place(x=20 , y= 140, width=130, height=40)
deck_builder_switch_page = tk.Label(options_frame, text='', bg='#c3c3c3')
deck_builder_switch_page.place(x=3, y=140, width=5, height =40)

profile_maker_button = ttk.Button(options_frame, text='Profile Maker', command=lambda: switch_page(profile_maker_switch_page, profile_maker_page))
profile_maker_button.place(x=20, y=200, width=130, height=40)
profile_maker_switch_page = tk.Label(options_frame, text='', bg='#c3c3c3')
profile_maker_switch_page.place(x=3, y=200, width=5, height=40)


window.mainloop()
