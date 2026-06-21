{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b9e0bd60-3a4c-4b8a-bcee-51d48cbb7723",
   "metadata": {},
   "outputs": [],
   "source": [
    "#1. Import Libraries\n",
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a0190c37-de8a-4e27-824f-848cf46a88f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#2. Load Datasets\n",
    "Student_Marks=pd.read_excel(\"C:\\\\Users\\\\mvr28\\\\Desktop\\\\ANVITHA\\\\PANDAS\\\\Marks.xlsx\",sheet_name=\"Student_Marks\")\n",
    "Student_Marks_with_Duplicates=pd.read_excel(\"C:\\\\Users\\\\mvr28\\\\Desktop\\\\ANVITHA\\\\PANDAS\\\\Marks.xlsx\",sheet_name=\"Student_Marks_Dirty\")\n",
    "Student_Details=pd.read_excel(\"C:\\\\Users\\\\mvr28\\\\Desktop\\\\ANVITHA\\\\PANDAS\\\\Marks.xlsx\",sheet_name=\"Student_Details\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9fdd5dcd-2704-441f-9dc1-b4bbc84fb066",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Roll_No      Name Branch  Telugu  English  Maths  Science  Social  Total  \\\n",
      "0       101   sundeep    CSE      90       85     80       83      75    413   \n",
      "1       102   saradhi    CSE      50       60     75       54      64    303   \n",
      "2       103    ramesh    ECE      95       78     68       58      78    377   \n",
      "3       104    suresh    CSE      55       87     68       64      59    333   \n",
      "4       105   sathwik    ECE      88       84     98       73      81    424   \n",
      "5       106   abhiram    CSE      73       84     91       88      84    420   \n",
      "6       107  srinidhi    ECE      90       83     74       86      94    427   \n",
      "7       108   lakshmi    CSE      75       78     85       64      53    355   \n",
      "8       109    dinesh    ECE      84       85     76       94      54    393   \n",
      "9       110    harish    CSE      83       98     81       63      79    404   \n",
      "10      111    murali    ECE      85       86     92       75      35    373   \n",
      "11      112      vasu    CSE      50       54     64       87      45    300   \n",
      "12      113      kali    ECE      89       97     69       73      82    410   \n",
      "13      114      ramu    CSE      25       45     60       35      48    213   \n",
      "14      115   krishna    EEE       1       25     65       50      55    196   \n",
      "15      116      hari    ECE      78       89     95       67      58    387   \n",
      "16      117     pavan    CSE      59       52     68       68      70    317   \n",
      "17      118     ashok    ECE      85       86     98       78      44    391   \n",
      "18      119    govind    CSE      89       89     95       66      95    434   \n",
      "19      120   bhargav    ECE      72       78     86       64      72    372   \n",
      "\n",
      "    Percentage       Grades  \n",
      "0         82.6  Distinction  \n",
      "1         60.6  First Class  \n",
      "2         75.4  First Class  \n",
      "3         66.6  First Class  \n",
      "4         84.8  Distinction  \n",
      "5         84.0  Distinction  \n",
      "6         85.4  Distinction  \n",
      "7         71.0  First Class  \n",
      "8         78.6  First Class  \n",
      "9         80.8  Distinction  \n",
      "10        74.6  First Class  \n",
      "11        60.0         Pass  \n",
      "12        82.0  Distinction  \n",
      "13        42.6         Pass  \n",
      "14        39.2         Fail  \n",
      "15        77.4  First Class  \n",
      "16        63.4  First Class  \n",
      "17        78.2  First Class  \n",
      "18        86.8  Distinction  \n",
      "19        74.4  First Class  \n"
     ]
    }
   ],
   "source": [
    "#3. Feature Engineering\n",
    "\n",
    "#Total\n",
    "Student_Marks[\"Total\"]=Student_Marks[\"Telugu\"]+Student_Marks[\"English\"]+Student_Marks[\"Maths\"]+Student_Marks[\"Science\"]+Student_Marks[\"Social\"]\n",
    "\n",
    "#Percentage Calculation\n",
    "Student_Marks[\"Percentage\"]= (Student_Marks[\"Total\"]/500)*100\n",
    "\n",
    "#Assign Grades\n",
    "Student_Marks[\"Grades\"]=\"Pass/Fail\"\n",
    "Student_Marks.loc[Student_Marks[\"Percentage\"]<40, [\"Grades\"]] = \"Fail\"\n",
    "Student_Marks.loc[(Student_Marks[\"Percentage\"]>=40) & (Student_Marks[\"Percentage\"]<=60), [\"Grades\"]] = \"Pass\"\n",
    "Student_Marks.loc[(Student_Marks[\"Percentage\"]>60) & (Student_Marks[\"Percentage\"]<=80), [\"Grades\"]] = \"First Class\" \n",
    "Student_Marks.loc[Student_Marks[\"Percentage\"]>80, [\"Grades\"]] = \"Distinction\"\n",
    "print(Student_Marks)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "291149e7-c7aa-454e-90c5-8fa0cdc59b4d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Roll_No    0\n",
      "Name       0\n",
      "Branch     0\n",
      "Telugu     0\n",
      "English    0\n",
      "Maths      1\n",
      "Science    1\n",
      "Social     1\n",
      "dtype: int64\n",
      "    Roll_No      Name Branch  Telugu  English  Maths  Science  Social\n",
      "0       101   sundeep    CSE      90       85   80.0     83.0    75.0\n",
      "1       102   saradhi    CSE      50       60   75.0     54.0    64.0\n",
      "2       103    ramesh    ECE      95       78   68.0     58.0    78.0\n",
      "3       104    suresh    CSE      55       87   68.0     64.0    59.0\n",
      "5       105   sathwik    ECE      88       84    NaN     73.0    81.0\n",
      "6       106   abhiram    CSE      73       84   91.0     88.0    84.0\n",
      "7       107  srinidhi    ECE      90       83   74.0      NaN    94.0\n",
      "8       108   lakshmi    CSE      75       78   85.0     64.0    53.0\n",
      "9       109    dinesh    ECE      84       85   76.0     94.0    54.0\n",
      "10      110    harish    CSE      83       98   81.0     63.0    79.0\n",
      "11      111    murali    ECE      85       86   92.0     75.0    35.0\n",
      "13      112      vasu    CSE      50       54   64.0     87.0     NaN\n"
     ]
    }
   ],
   "source": [
    "#4. Data Cleaning\n",
    "\n",
    "Student_Marks_with_Duplicates=pd.read_excel(\"C:\\\\Users\\\\mvr28\\\\Desktop\\\\ANVITHA\\\\PANDAS\\\\Marks.xlsx\",sheet_name=\"Student_Marks_Dirty\")\n",
    "\n",
    "#Check missing values\n",
    "Missing_Values = Student_Marks_with_Duplicates.isnull().sum()\n",
    "print(Missing_Values)\n",
    "\n",
    "# Remove duplicate rows\n",
    "Remove_Duplicate_rows = Student_Marks_with_Duplicates.drop_duplicates()\n",
    "print(Remove_Duplicate_rows)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5e417f01-2683-4d92-992a-f45d1a008864",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Roll_No      Name Branch  Telugu  English  Maths  Science  Social  Total  \\\n",
      "0       101   sundeep    CSE      90       85     80       83      75    413   \n",
      "1       102   saradhi    CSE      50       60     75       54      64    303   \n",
      "2       103    ramesh    ECE      95       78     68       58      78    377   \n",
      "3       104    suresh    CSE      55       87     68       64      59    333   \n",
      "4       105   sathwik    ECE      88       84     98       73      81    424   \n",
      "5       106   abhiram    CSE      73       84     91       88      84    420   \n",
      "6       107  srinidhi    ECE      90       83     74       86      94    427   \n",
      "7       108   lakshmi    CSE      75       78     85       64      53    355   \n",
      "8       109    dinesh    ECE      84       85     76       94      54    393   \n",
      "9       110    harish    CSE      83       98     81       63      79    404   \n",
      "10      111    murali    ECE      85       86     92       75      35    373   \n",
      "11      112      vasu    CSE      50       54     64       87      45    300   \n",
      "12      113      kali    ECE      89       97     69       73      82    410   \n",
      "13      114      ramu    CSE      25       45     60       35      48    213   \n",
      "14      115   krishna    EEE       1       25     65       50      55    196   \n",
      "15      116      hari    ECE      78       89     95       67      58    387   \n",
      "16      117     pavan    CSE      59       52     68       68      70    317   \n",
      "17      118     ashok    ECE      85       86     98       78      44    391   \n",
      "18      119    govind    CSE      89       89     95       66      95    434   \n",
      "19      120   bhargav    ECE      72       78     86       64      72    372   \n",
      "\n",
      "    Percentage       Grades        City      Phone  \n",
      "0         82.6  Distinction  Vijayawada  900000001  \n",
      "1         60.6  First Class      Guntur  900000002  \n",
      "2         75.4  First Class   Hyderabad  900000003  \n",
      "3         66.6  First Class     Chennai  900000004  \n",
      "4         84.8  Distinction   Bangalore  900000005  \n",
      "5         84.0  Distinction  Vijayawada  900000006  \n",
      "6         85.4  Distinction      Guntur  900000007  \n",
      "7         71.0  First Class   Hyderabad  900000008  \n",
      "8         78.6  First Class     Chennai  900000009  \n",
      "9         80.8  Distinction   Bangalore  900000010  \n",
      "10        74.6  First Class  Vijayawada  900000011  \n",
      "11        60.0         Pass      Guntur  900000012  \n",
      "12        82.0  Distinction   Hyderabad  900000013  \n",
      "13        42.6         Pass     Chennai  900000014  \n",
      "14        39.2         Fail   Bangalore  900000015  \n",
      "15        77.4  First Class  Vijayawada  900000016  \n",
      "16        63.4  First Class      Guntur  900000017  \n",
      "17        78.2  First Class   Hyderabad  900000018  \n",
      "18        86.8  Distinction     Chennai  900000019  \n",
      "19        74.4  First Class   Bangalore  900000020  \n"
     ]
    }
   ],
   "source": [
    "#5. Merge Datasets\n",
    "#Merge Student_Marks and Student_Details using Roll_No.\n",
    "Merged = pd.merge(Student_Marks, Student_Details, on=\"Roll_No\")\n",
    "print(Merged)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f66b28e6-efd5-41ed-b5f6-a74921f3ddcb",
   "metadata": {},
   "outputs": [],
   "source": [
    "#6. Export Report\n",
    "Merged.to_excel(\"C:\\\\Users\\\\mvr28\\\\Desktop\\\\ANVITHA\\\\PANDAS\\\\Final_Student_Report.xlsx\",index=False)\n",
    "\n",
    "#export in csv\n",
    "Merged.to_csv(\"C:\\\\Users\\\\mvr28\\\\Desktop\\\\ANVITHA\\\\PANDAS\\\\Final_Student_Report.csv\",index=False)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
