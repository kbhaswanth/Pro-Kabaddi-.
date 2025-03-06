import streamlit as st
import pandas as pd

# Data for PKL seasons
data = {
    'Season': ['Season 1', 'Season 2', 'Season 3', 'Season 4', 'Season 5',
               'Season 6', 'Season 7', 'Season 8', 'Season 9', 'Season 10', 'Season 11'],
    'Year': [2014, 2015, 2016, 2016, 2017, 2018, 2019, 2021, 2022, 2023, 2024],
    'Winner': ['Jaipur Pink Panthers', 'U Mumba', 'Patna Pirates', 'Patna Pirates',
               'Patna Pirates', 'Bengaluru Bulls', 'Bengal Warriors', 'Dabang Delhi',
               'Jaipur Pink Panthers', 'Puneri Paltan', 'Haryana Steelers'],
    'Runner-up': ['U Mumba', 'Bengaluru Bulls', 'U Mumba', 'Jaipur Pink Panthers',
                  'Gujarat Giants', 'Gujarat Giants', 'Dabang Delhi', 'Patna Pirates',
                  'Puneri Paltan', 'Haryana Steelers', 'Patna Pirates'],
    'Score': ['35–24', '36–30', '31–28', '37–29', '55–38', '38–33', '39–34',
              '37–36', '33–29', '28–25', '32–23']
}
df = pd.DataFrame(data)

# Player statistics
players = {
    'Player': ['Pardeep Narwal', 'Fazel Atrachali'],
    'Achievement': ['Most raid points (1,801 in 177 matches)',
                    'Most tackle points (524 in PKL history)']
}
pf = pd.DataFrame(players)

# Streamlit app
def main():
    st.title('Pro Kabaddi League Overview')
    
    # Display PKL logo (Using direct image link)
    st.image('https://www.prokabaddi.com/', 
             caption='Pro Kabaddi League', use_container_width=True)
    
    # Display PKL Seasons and Winners
    st.header('PKL Seasons and Winners')
    st.table(df)
    
    # Player Achievements
    st.header('Notable Player Achievements')
    st.table(pf)
    
    # Player images
    st.subheader('Top Players')
    col1, col2 = st.columns(2)
    
    with col1:
        st.image('https://www.prokabaddi.com/static-assets/images/players/197.png?v=6.86', 
                 caption='Pardeep Narwal', use_container_width=True)
    with col2:
        st.image('https://www.prokabaddi.com/static-assets/images/players/259.png?v=6.86', 
                 caption='Fazel Atrachali', use_container_width=True)

if __name__ == "__main__":
    main()
