import matplotlib.pyplot as plt
import pandas as pd

data = {'Name' : ['Aadil', 'Pratik', 'Aman', 'Alam', 'Jahanvi', 'Janhvi','Saanvi'],
        'Gender': ['Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Female'],
        'Age': [19, 35, 45, 28, 20, 60, 25]}

df = pd.DataFrame(data)

#Graph for Gender Distrbution
gender_counts = df['Gender'].value_counts()

plt.bar(gender_counts.index, gender_counts.values, color=['blue', 'pink'])
plt.title('Gender Distribution in Population')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Graph for Age Distrbution
age_counts = df['Age'].value_counts()
age_counts = age_counts.sort_index()

plt.hist(df['Age'], bins=5, edgecolor='black', color='green')
plt.title('Age Distribution in Population')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()


