# ----------------------------------------------------------------------
# Experiment 11: Log file reader
# ----------------------------------------------------------------------
LOG_LEVELS = ("INFO", "WARNING", "ERROR")


def create_sample_log(filename):
    lines = [f"2026-09-02 10:{i:02d}:00 INFO Task {i} completed" for i in range(14)]
    lines += [f"2026-09-02 11:{i:02d}:00 WARNING Disk usage high" for i in range(3)]
    lines += [f"2026-09-02 12:{i:02d}:00 ERROR Connection failed" for i in range(2)]
    with open(filename, "w") as f:
        f.write("\n".join(lines) + "\n")


def parse_log_file(filename):
    counts = {level: 0 for level in LOG_LEVELS}
    try:
        with open(filename, "r") as file:
            for line in file:
                for level in LOG_LEVELS:
                    if level in line:
                        counts[level] += 1
                        break
    except FileNotFoundError:
        print("Error: Target log file does not exist.")
        return
    print("----- LOG SUMMARY -----")
    for level, total in counts.items():
        print(f"{level}: {total}")


def experiment_11():
    filename = input("Enter log file name (press Enter for a sample log): ").strip()
    if not filename:
        filename = "sample_app.log"
        create_sample_log(filename)
    parse_log_file(filename)


# ----------------------------------------------------------------------
# Experiment 12: Student data manager using files
# ----------------------------------------------------------------------
STUDENT_FILE = "students.txt"


def student_exists(usn):
    if not os.path.exists(STUDENT_FILE):
        return False
    with open(STUDENT_FILE, newline="") as f:
        return any(row and row[0] == usn for row in csv.reader(f))


def add_student(usn, name, dept):
    if student_exists(usn):
        print(f"Student {usn} already exists - skipped.")
        return
    with open(STUDENT_FILE, "a", newline="") as f:
        csv.writer(f).writerow([usn, name, dept])
    print("Student record added successfully!")


def display_students():
    print("\n----- STUDENT RECORDS -----")
    if not os.path.exists(STUDENT_FILE):
        print("No records found.")
        return
    with open(STUDENT_FILE, newline="") as f:
        for row in csv.reader(f):
            if len(row) == 3:
                print(f"USN: {row[0]} | Name: {row[1]} | Dept: {row[2]}")


def experiment_12():
    add_student("25BTRAD113", "Sushanth", "CSE")
    add_student("25BTRAD124", "Rahul", "ECE")
    display_students()


# ----------------------------------------------------------------------
# Experiment 13: CSV-based payroll management system
# HRA = 20% of basic, DA = 10% of basic, PF = 12% of basic
# ----------------------------------------------------------------------
def create_sample_payroll(filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["EmpID", "Name", "BasicSalary"])
        writer.writerow(["E101", "Sushanth", 50000])
        writer.writerow(["E102", "Anand", 62000])


def generate_payroll(csv_filename):
    print("\n----- PAYROLL SALARY SUMMARY -----")
    try:
        with open(csv_filename, mode="r", newline="") as file:
            for row in csv.DictReader(file):
                try:
                    basic = float(row["BasicSalary"])
                except (ValueError, KeyError):
                    print(f"Skipping invalid record: {row}")
                    continue
                gross = basic + basic * 0.20 + basic * 0.10
                pf = basic * 0.12
                net = gross - pf
                print(f"ID: {row['EmpID']} | Name: {row['Name']} | "
                      f"Gross: {gross:.2f} | PF: {pf:.2f} | Net Salary: {net:.2f}")
    except FileNotFoundError:
        print(f"Error: '{csv_filename}' not found.")


def experiment_13():
    if not os.path.exists("payroll.csv"):
        create_sample_payroll("payroll.csv")
    generate_payroll("payroll.csv")
