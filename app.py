import streamlit as st
import pandas as pd

@st.cache_data

def load_data():
    return pd.read_csv('energy-and-mining_ken.csv')

df = load_data()

st.set_page_config(
    page_title = 'Kenyan Energy Evolution',
    page_icon = '⚡', #lighting emoji
    layout = 'wide'
)

st.title('⚡ Overview of Energy Evolution from 1990-2021')

st.markdown('''
            This dashboard examines the Kenya's shift in energy universal access to national intesisty and efficiency to real world impacts on business
             ''')


tab1, tab2 ,tab3, tab4 = st.tabs(['📊Social Equality', '📈Economic Efficiency', '💼Business Tax', '💡My Recommendations'])

with tab1:
    st.header('Rural vs Urban Electricity Access')
    st.write('Analysis of how energy access has been distributed accross the country')
    #filtering 
    rural_df = df[df['Indicator Name'] == 'Access to electricity, rural (% of rural population)'][['Year', 'Value']].rename(columns={'Value': 'Rural Access'})
    urban_df = df[df['Indicator Name'] == 'Access to electricity, urban (% of urban population)'][['Year', 'Value']].rename(columns={'Value': 'Urban Access'})
    combined_df= pd.merge(rural_df, urban_df, on='Year')
    st.line_chart(combined_df.set_index('Year'))
    st.divider()
    st.subheader('Insight:Gap closing')
    st.info('''
                The line chart shows a narrowing of the energy access gap between rural and urban as a direct result of the **Last mile connectivity project**, which extends the grid to off-grid rural regions

                **importance** we  see an all national inclusivity and decentralization of business opportunity with time
                ''')
    st.caption('Data source: https://www.kplc.co.ke/last-mile-connectivity')

with tab2:
    st.header('Energy use per $1000 GDP')
    st.write('Decoupling economic growth from energy consumption (MJ/$)')
    energy_intensity = df[df['Indicator Name'] == 'Energy intensity level of primary energy (MJ/$2021 PPP GDP)'][['Year', 'Value']].rename(columns={'Value':'MJ/$ GDP'})
    st.line_chart(energy_intensity.set_index('Year'))

    
    st.divider()
    st.subheader('Insight: Efficiency Trend')
    st.divider()
    st.markdown('**Energy intensity (MJ/$)** tracks the amount of energy required to produce a unit of GDP')

    st.divider() 

    col1,col2 = st.columns(2)
    
    with col1:
        st.subheader('Phase 1')
        st.write('''# **Investment programs and various developemts**
                    - several geothamal power plants in olkaria with `745mw` capaticy - some completed
                    - Upgdaing of kindaruma plant - completed
                    - Lake Turkana Wind Power Project Producing `310mw` -completed aroudn 2018
                ''')
        st.caption ('I phase1:  https://www.knbs.or.ke/wp-content/uploads/2023/09/2014-Economic-Survey.pdf')

    with col2:
        st.subheader('Phase 2')
        st.write('''# **Cooling period**
                    - Lake Turkana Wind Power Project - complete
                    - Garissa Solar Power Plant `50mw` - complete 2019
                    - Kopere Solar Park producing `50mw` - complete 2016
                ''')
        st.caption(''' 

            turkana: https://ltwp.co.ke/

            Garissa Solar : https://www.rerec.co.ke/garissa-solar-power-plant.php

            Kopere Solar :  https://www.afdb.org/fileadmin/uploads/afdb/Documents/Environmental-and-Social-Assessments/Kenya_-_Kopere_Solar_Park_Power_Project_in_Kisumu_District__Nandi_County_%E2%80%93_ESIA_Summary.pdf
            ''')


    
   
    st.divider()
    
    col1,col2 =st.columns(2)
    first = energy_intensity['MJ/$ GDP'].iloc[-1]
    final =  energy_intensity['MJ/$ GDP'].iloc[0]
    with col1:
        st.metric(f'First recorded value (MJ/$):',  f'{first: .2f}')
    with col2:
        st.metric(f'Last recorded value (MJ/$):' , f'{final: .2f}' ) 
    if final < first :
        st.success('**efficiency success:** Kenya is successfully decoupling growth from energy consumption')
    else:
        st.success('Improvements in the energy sector still need improving')

with tab3: 
    st.header('Hidden tax of Energy instability ')
    st.divider()
    st.markdown('''
                Reliable electricity is not just a utility , its the backbone of industrial production 
                * **Lost of productivity** Downtime during outages**
                * **Operation overhead** High cost of maintaining a backup generators
                * **The trend we observe in tab1 showing universal access and tab2 efficiency over time and finally competitive barriers in bussiness enviroment''')
    
    st.divider()
    outage_df = df[df['Indicator Name'] == 'Value lost due to electrical outages (% of sales for affected firms)'][['Year', 'Value']].rename(columns={'Value':'Outages'})
    connect_df = df[df['Indicator Name'] == 'Time to obtain an electrical connection (days)'][['Year', 'Value']].rename(columns={'Value': 'Time to connect'})
    business_df = pd.merge(outage_df, connect_df, on='Year')
    st.scatter_chart(business_df, x='Outages', y='Time to connect', color='Year')
    st.divider()
    st.caption (''' In this correlation between the "hidden tax" of outages and connection delays
                the color gradient helps us see the business environment , if moving to the bottom left shows improved reliabity
                if dots are clustering at a lower point over time , indicates policy intervention is working''')
    

with tab4:
    st.header('Policy & Strategy i can think of')

    col1,col2 = st.columns(2)

    with col1:
        st.subheader('For the energy sector')
        st.caption('''
                * **Decentralized Solar:** Prioritize solar kits for remote rural areas instead of expensive gridlines
                 
                * **Grid optimization:** Focus on rehabilitation and smart-metering to reduce distribution losses
                ''')
        
    with col2:
        st.subheader('For the private sector')
        st.caption('''
                * **Solar Incentives:** Providing low-interest financing options for smes to install rooftop solar
                  
                * **Energy Audits:** Promote regular audits to help the industries be modernized
                ''')
        
    st.divider()
    
    st.info('## conlclusion With this Energy data we see while access is increasing realiabity still remains a primary contention for economic growth. This intern shows that renawable adaptability and efficiency in the energy opeations are key to sustainable Kenyan energy future')
