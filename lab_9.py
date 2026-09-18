import cv2
import numpy as np
import heapq
from collections import Counter

class Node:
    def __init__(self, frequency, pixel_value, left=None, right=None):
        self.frequency = frequency
        self.pixel_value = pixel_value
        self.left = left
        self.right = right
        self.code = ''

    def __lt__(self, other):
        return self.frequency < other.frequency

huffman_codes = {}

def generate_codes(node, current_code=''):
    new_code = current_code + str(node.code)
    if node.left:
        generate_codes(node.left, new_code)
    if node.right:
        generate_codes(node.right, new_code)
    if not node.left and not node.right:
        huffman_codes[node.pixel_value] = new_code

image = cv2.imread('lab_1_image.jpg', 0)

if image is None:
    print("Couldn't read image")
else:
    print("Image loaded successfully.")
    flat_image = image.flatten()
    pixel_counts = Counter(flat_image)
    print("Pixel frequencies calculated")
    nodes = []
    for pixel, count in pixel_counts.items():
        heapq.heappush(nodes, Node(count, pixel))

    while len(nodes) > 1:
        left_node = heapq.heappop(nodes)
        right_node = heapq.heappop(nodes)

        left_node.code = 0
        right_node.code = 1

        combined_frequency = left_node.frequency + right_node.frequency
        new_parent_node = Node(combined_frequency, "Combined", left_node, right_node)
        heapq.heappush(nodes, new_parent_node)
    print("Huffman tree constructed")

    root_node = nodes[0]
    generate_codes(root_node)

    print("Binary codes generated")

    original_size = len(flat_image) * 8
    compressed_size = 0
    for pixel, count in pixel_counts.items():
        code_length = len(huffman_codes[pixel])
        compressed_size += code_length * count

    print("Original size:", original_size)
    print("Compressed size:", compressed_size)
    compression_ratio = original_size / compressed_size
    print("Compression ratio:", compression_ratio)