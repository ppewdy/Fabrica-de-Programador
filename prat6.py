import streamlit as st

st.sidebar.image('theking.jpg')
st.sidebar.title("you're my sunshine")

st.sidebar.image('theaustralianking.jpg')
st.sidebar.title("you're my sunshine")

para = st.sidebar.image('theegypcianking.jpg')
st.sidebar.title("you're my sunshine")

conls = st.columns(2)

conls[0].image('theking.jpg')
if st.button('LeeBro'):
    conls[1].write("you're my sunshine")
    conls[1].write('You make me happy when skies are grey')
    conls[1].write("You'll never know, dear, how much I love you")
    conls[1].write("Please, don't take my sunshine away")
    conls[1].write("I've always loved you and made you happy")
    conls[1].write("And nothing else could come between")
    conls[1].write("But now you've left me to love another")
    conls[1].write("You have shattered all of my dreams")
    


