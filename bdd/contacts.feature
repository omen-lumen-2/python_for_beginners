Scenario Outline: Add new contact
  Given a raw contact list
  Given a contact with <firstname>, <middlename>
  When i create new contact
  Then the new contact list is equal to raw contact list with created contact

  Examples:
  | firstname | middlename |
  | Test1      | Test2     |
  | None       | None      |


Scenario: Delete contact
  Given there must be at least one contact
  Given a raw contact list
  Given choice random contact
  When i delete selected contact
  Then the new contact list is equal to raw contact list without deleted contact

Scenario: Update contact
  Given there must be at least one contact
  Given a raw contact list
  Given choice random contact
  Given a new data for contact
  When i update selected contact
  Then the new contact list is equal to raw contact list without update contact