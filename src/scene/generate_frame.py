def generate_frame(frame):
    with open("../output/ppm_frames/frame.ppm", "w") as file:
        file.write(frame)

    print("Successfully generated frame.")
