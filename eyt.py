import time

def loading_animation():
    print("පද්ධතිය ආරම්භ වේ...", end="")
    
    # මෙතනින් වෙන්නේ කෝඩ් එක පොඩ්ඩ පොඩ්ඩ පෙන්වන එක
    for i in range(5):
        print(i, end=" ")
        time.sleep(0.5) # තත්පර භාගයක් නවතිනවා
        
    print("\nසාර්ථකයි! පයිතන් සාදරයෙන් පිළිගන්නවා, Ishan! 🚀")

loading_animation()