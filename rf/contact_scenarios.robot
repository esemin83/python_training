*** Settings ***
Library  rf.Addressbook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new contact
    ${old_list}=  Get Contact List
    ${cont}=  New Contact  firstname  middlename  lastname  address  email  phone
    Create Contact  ${cont}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  ${cont}
    Contact Lists Should Be Equal  ${old_list}  ${new_list}

Delete contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${cont}=  Get From List  ${old_list}  ${index}
    Delete Contact  ${cont}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${cont}
    Contact Lists Should Be Equal  ${old_list}  ${new_list}

Modify contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${x}=  Get From List  ${old_list}  ${index}
    ${cont}=  New Contact  firstname2  middlename2  lastname2  address2  email2  phone2
    Modify Contact  ${cont}  ${x}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${x}
    Append To List  ${old_list}  ${cont}
    #Insert Into List  ${old_list}  ${x}  ${cont}
    Contact Lists Should Be Equal  ${old_list}  ${new_list}