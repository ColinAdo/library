from core.forms import ReviewForm

class TestForm:
    def test_form_valid(self):
        data = {'comment': 'Test comment'}
        form = ReviewForm(data=data)

        assert form.is_valid()

    def test_form_errors(self):
        data = {'comment': ''}
        form = ReviewForm(data=data)

        assert 'comment' in form.errors
        assert 'This field is required.' in form.errors['comment']
