"""
A skeleton python script which reads from an input file,
writes to an output file and parses command line arguments
"""
import os
from PyPDF2 import PdfFileMerger

def main():
    input_path = "input_files"
    res_flag = True

    while res_flag:
        if os.path.isdir(input_path) and len(os.listdir(input_path)) > 0:
            for i,file in enumerate(os.listdir(input_path)):
                print(f"[{i+1}] {file}")
            
        res = input("Are the pdf files in the right order?").lower()
    #     print(res)
        if res in {'y', 'yes'}:
            print("merging pdfs...")
            merge_list = []

            for x in os.listdir(input_path):
                if not x.endswith('.pdf'):
                    continue
                merge_list.append(os.path.join(input_path,x))

            merger = PdfFileMerger()

            for pdf in merge_list:
                merger.append(pdf)
            pdf_file = "merged_pdf.pdf"
            merger.write(pdf_file) #your output directory
            merger.close()
            print(f"pdfs merged as {pdf_file}")
            res_flag = False
        else:
            print("Ensure files in directory, \input_files is in name order")
            print("When ready to check again, press any button to continue or press Q to quit")
            check = input("Are you ready to check again?").lower()
            if check == 'q':
                print("quitting")
                res_flag = False
                quit()
            else:
                pass
    



if __name__ == "__main__":
    main()