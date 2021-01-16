Feature: Login OrangeHRM

  Scenario: Login to OrangeHRM with valid parameters
    Given I launch Chrome Browser
    When I open orange HRM homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must successfully login to the Dashboard page

  Scenario: Search user
    Given I launch Chrome Browser
    When I open orange HRM homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    When navigate to search page
    Then search page should display

  Scenario: Advanced Search
    Given I launch Chrome Browser
    When I open orange HRM homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    When navigate to advanced search page
    Then adcanced search page should display