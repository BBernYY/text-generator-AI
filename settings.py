model = {
    "params": "1.3B" # 125M, 1.3B or 2.7B
}
generate = {
    "text_inputs": open("input.txt", "r").read(),
    "max_length": 250,
    "do_sample": True,
    "temperature": 0.9
}
