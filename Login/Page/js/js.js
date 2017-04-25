class AdminPanelViewModel
  constructor: () ->
    @displayTab = ko.observable('users')
    @collapsedNav = ko.observable(false)
  changeTab: (tab) =>
    @displayTab(tab)
  collapse: () =>
    @collapsedNav(!@collapsedNav())
    
$ ->
  ko.applyBindings(new AdminPanelViewModel())