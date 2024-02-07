# from checker import check_for_updates
# import streamlit as st

# st.title('URL Monitor')

# if st.button('Check for Updates'):
#     updated_urls = check_for_updates()
#     if updated_urls:
#         st.write('Changes detected in the following URLs:')
#         for name in updated_urls:
#             st.write(name)
#     else:
#         st.write('No changes detected.')
from checker import check_for_updates
import streamlit as st

st.title('URL Monitor')

if st.button('Check for Updates'):
    updates_info = check_for_updates()
    if updates_info:
        st.write('Changes detected in the following URLs:')
        for update in updates_info:
            name, url = update['name'], update['url']
            st.write(f"{name}: [View Update]({url})")
    else:
        st.write('No changes detected.')
