# Created by jessi at 11/29/2021
Feature: Test cases for top banner functionality

  Scenario: User can click right and left arrows to see top banners
    Given Open Gettop main page
    When Hover over the top banner
    And Click the right arrow icon
    And Store product name
    And Click the left arrow icon
    Then Verify different products were seen
#
#  Scenario: User can click bottom dots to see top banners
#    Given Open Gettop main page
#    When Hover over top banner
#    And Click the bottom right dot
#    And Store product name
#    And Click the bottom left dot
#    And Store product name
#    Then Verify different products were seen
#
#  Scenario: User can click on product banner and is taken to correct category page
#    Given Open Gettop main page
#    Then User can click through banner links and verify correct page opens




