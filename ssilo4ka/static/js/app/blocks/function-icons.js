$('.function').on('mouseover', function() {
    $(this).find('svg').children().css({
      'color': 'black',
    });
  });
  $('.function').on('mouseleave', function() {
    $(this).find('svg').children().css({
      'color':'grey',
    });
  });