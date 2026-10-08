def main():
    with open("alice.txt",) as f:
        # contents = f.read()
        contents = f.readlines()
        # print(f"hello {contents}")
        print(contents)
    # print(contents[52:272])
    # with open("chapter_I","w") as f:
        # f.writelines(contents[52:272])
main()
