from main import app
import ldap

def authenticate(username, password):
    LDAP_SERVER = 'ldap://xx'
    LDAP_USERNAME = 'DOMAIN\\%s' % username
    LDAP_PASSWORD = password

    # Tries to validate user with LDAP-bind, returns OK if valid
    try:
        ldap_client = ldap.initialize(LDAP_SERVER)
        ldap_client.set_option(ldap.OPT_REFERRALS,0)
        ldap_client.simple_bind_s(LDAP_USERNAME, LDAP_PASSWORD)
    except:
        ldap_client.unbind()
        return 'PASSWORD_ERROR'
        
    ldap_client.unbind()
    return 'OK'
