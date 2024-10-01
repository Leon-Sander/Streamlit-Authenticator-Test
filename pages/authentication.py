import streamlit as st
import streamlit_authenticator as stauth

CONFIG_FILENAME = 'auth_config.yaml'


#with open(CONFIG_FILENAME) as file:
#    config = yaml.load(file, Loader=SafeLoader)

st.header('Account page')


authenticator = stauth.Authenticate(CONFIG_FILENAME)

login_tab, register_tab = st.tabs(['Login', 'Register'])

with login_tab:
    authenticator.login(location='main')

    if st.session_state["authentication_status"]:
        st.session_state.authenticator_object = authenticator
        #st.switch_page('app.py')
        authenticator.logout(location='main')    
        st.write(f'Welcome *{st.session_state["name"]}*')

    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')

with register_tab:
    #It is 8-20 characters, one lowercase letter, one uppercase, one number AND one special character (@$!%*?&)
    if not st.session_state["authentication_status"]:
        try:
            #config['pre-authorized']["emails"]
            email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(pre_authorized=["test1@test.com"])
            if email_of_registered_user:
                st.success('User registered successfully')
        except Exception as e:
            st.error(e)