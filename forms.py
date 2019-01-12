from datetime import time

from django import forms

from .models import TVProgram


class TVProgramForm(forms.Form):
    hours = [(h, "{:02d}".format(h)) for h in (range(0, 24))]
    minutes = [(m, "{:02d}".format(m)) for m in ((0, 15, 30, 45))]
    title = forms.CharField(label='TV Program Title', max_length=200)
    start_hour = forms.ChoiceField(label='Start Hour', choices=hours)
    start_minute = forms.ChoiceField(label='Start Minute', choices=minutes)
    end_hour = forms.ChoiceField(label='End Hour', choices=hours)
    end_minute = forms.ChoiceField(label='End Minute', choices=minutes)

    def clean(self):
        """
        Verifies times are in the correct order and queries TV programs to make
        sure there are not conflicting times.
        """
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        start_hour = int(cleaned_data.get('start_hour'))
        start_minute = int(cleaned_data.get('start_minute'))
        end_hour = int(cleaned_data.get('end_hour'))
        end_minute = int(cleaned_data.get('end_minute'))

        start_time = time(start_hour, start_minute, 0)
        end_time = time(end_hour, end_minute, 59)

        if start_time >= end_time:
            message = "End time should be after start time."
            raise forms.ValidationError(message, code='time_reversed')

        count_conflicting_programs = TVProgram.objects.filter(
            start_time__gte=start_time,
            end_time__lte=end_time
            ).count()

        if count_conflicting_programs > 0:
            message = "TV Program ({}, {:02d}:{:02d} to {:02d}:{:02d}) conflicts with another program.".format(
                title,
                start_hour,
                start_minute,
                end_hour,
                end_minute
            )
            raise forms.ValidationError(message, code='time_overlap')

    def save(self):
        title = self.cleaned_data['title']
        start_time = time(
            int(self.cleaned_data['start_hour']),
            int(self.cleaned_data['start_minute']),
            0
        )
        end_time = time(
            int(self.cleaned_data['end_hour']),
            int(self.cleaned_data['end_minute']),
            59
        )
        tv_program = TVProgram(
            title=title,
            start_time=start_time,
            end_time=end_time
        )
        tv_program.save()
        return tv_program
