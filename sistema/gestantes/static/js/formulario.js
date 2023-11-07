$(document).ready(() => {
    const scroll_to_class = (element_class, removed_height = 0) => {
        let scroll_to = $(element_class).offset().top - removed_height;
        $('html, body').stop().animate({scrollTop: scroll_to}, 500);
    }

    const bar_progress = (progress_line_object, direction) => {
        let number_of_steps = progress_line_object.data('number-of-steps');
        let now_value = progress_line_object.data('now-value');
        let step = 100 / number_of_steps;
        let new_value = (direction === 'right') ? now_value + step : now_value - step;
        new_value = Math.max(0, Math.min(new_value, 100));
        progress_line_object.attr('style', 'width: ' + new_value + '%;').data('now-value', new_value);
    }

    $('.f1 fieldset:first').fadeIn('slow');
    $('.f1 input[type="text"], .f1 input[type="password"], .f1 input[type="file"], .f1 input[type="date"], .f1 input[type="number"], .f1 textarea, f1 select').on('focus', function() {
        $(this).removeClass('input-error');
    });

    $('.f1 .btn-next').on('click', function() {
        let parent_fieldset = $(this).parents('fieldset');
        let next_step = true;
        parent_fieldset.find('input[type="text"], input[type="password"], input[type="file"],input[type="date"],input[type="number"], textarea, select').each(function() {
            if ($(this).val().trim() === "") {
                $(this).addClass('input-error');
                next_step = false;
            } else {
                $(this).removeClass('input-error');
            }
        });

        if (next_step) {
            parent_fieldset.fadeOut(400, function() {
                let current_active_step = $(this).parents('.f1').find('.f1-step.active');
                let progress_line = $(this).parents('.f1').find('.f1-progress-line');
                current_active_step.removeClass('active').addClass('activated').next().addClass('active');
                bar_progress(progress_line, 'right');
                $(this).next().fadeIn();
                scroll_to_class('.f1', 20);
            });
        }
    });

    $('.f1 .btn-previous').on('click', function() {
        let current_active_step = $(this).parents('.f1').find('.f1-step.active');
        let progress_line = $(this).parents('.f1').find('.f1-progress-line');

        $(this).parents('fieldset').fadeOut(400, function() {
            current_active_step.removeClass('active').prev().removeClass('activated').addClass('active');
            bar_progress(progress_line, 'left');
            $(this).prev().fadeIn();
            scroll_to_class('.f1', 20);
        });
    });

	
    $('.f1').on('submit', function(e) {
        $(this).find('input[type="text"], input[type="password"], input[type="file"],input[type="date"],input[type="number"], textarea, select').each(function() {
            if ($(this).val().trim() === "") {
                e.preventDefault();
                $(this).addClass('input-error');
            } else {
                $(this).removeClass('input-error');
            }
        });
    });
});