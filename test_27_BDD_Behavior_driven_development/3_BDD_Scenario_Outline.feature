Feature: Login OrangeHRM

  Scenario Outline: Login to OrangeHRM with valid parameters
    Given I launch Chrome Browser
    When I open orange HRM homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must successfully login to the Dashboard page

    Examples:
      | username | password |
      | admin    | admin    |
      | admin123 | admin123 |
      | admin222 | admin222 |