from Service.service import Service
def main():
    s = Service()
    s.import_data()
    print(s.courses)
    print(s.students)

if __name__ == "__main__":
    main()