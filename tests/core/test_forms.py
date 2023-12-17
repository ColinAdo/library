from core.forms import ReviewForm

class TestForm:
    def setup_method(self):
        self.valid_data = {'comment': 'Test comment'}
        self.invalid_data = data = {'comment': ''}
        
    def test_form_valid(self):
        form = ReviewForm(data=self.valid_data)

        assert form.is_valid()

    def test_form_errors(self):
        
        form = ReviewForm(data=self.invalid_data)

        assert 'comment' in form.errors
        assert 'This field is required.' in form.errors['comment']
