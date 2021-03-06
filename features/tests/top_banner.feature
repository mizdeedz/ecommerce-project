# Created by jessi at 11/29/2021
Feature: Test cases for top banner functionality

  Scenario: User can click right and left arrows to see top banners
    Given Open Gettop main page
    When Hover over the top banner
    And Click the right arrow icon
    And Store next product name
    And Click the left arrow icon
    And Store first product name
    Then Verify different products were seen

  Scenario: User can click bottom dots to see top banners
    Given Open Gettop main page
    When Hover over the top banner
    And Click the bottom right dot
    And Store next product name
    And Click the bottom left dot
    And Store first product name
    Then Verify different products were seen

  Scenario: User can click on product banner and is taken to correct category page
    Given Open Gettop main page
    Then User can click through banner links and verify correct page opens

  @mobile
  Scenario: User can swipe right and left to see top banners
    Given Open Gettop main page
    When Swipe left on banner
    And Store next product name
    And Swipe right on banner
    And Store first product name
    Then Verify different products were seen

  @mobile
  Scenario: User can tap on product banner and is taken to correct category page
    Given Open Gettop main page
    Then User can tap through banner links and verify correct page opens
