'''Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral! You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.

The pixels in the input image are represented as integers. The algorithm distorts the input image in the following way: Every pixel x in the output image has a value equal to the average value of the pixel values from the 3X3 square that has its center at x, including x itself. All the pixels on the border of x are then removed.

Return the blurred image as an integer, with the fractions rounded down.'''

def solution(image):
    avrg = 0
    output_frame = []
    for l in range(len(image) - 2):
        output_frameline = []
        for section in range(3):
            if section + 2 < len(image[l]):
                frame_section = []
                for ls in range(l, l + 3):
                    if ls < len(image):
                        frame_section.append(image[ls][section:section + 3])
            else:
                break
            s = 0
            for i in frame_section:
                s += sum(i)
            avrg = s // 9
            output_frameline.append(avrg)
        output_frame.append(output_frameline)
    return output_frame

if __name__ == '__main__':
    image = [[7, 4, 0, 1], 
         [5, 6, 2, 2], 
         [6, 10, 7, 8], 
         [1, 4, 2, 0]]
    print(solution(image))