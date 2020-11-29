import time

from starlette.responses import PlainTextResponse


def test_async_validator_success(app, client, FormWithAsyncValidators):
    @app.route('/', methods=['POST'])
    async def index(request):
        form = await FormWithAsyncValidators.from_formdata(request)
        assert form.field1.data == 'value1'
        assert form.field2.data == 'value2'

        # validate and check again
        await form.validate()
        assert form.field1.data == 'value1'
        assert form.field2.data == 'value2'

        return PlainTextResponse()

    client.post('/', data={'field1': 'value1', 'field2': 'value2'})


def test_async_validator_error(app, client, FormWithAsyncValidators):
    @app.route('/', methods=['POST'])
    async def index(request):
        form = await FormWithAsyncValidators.from_formdata(request)
        assert form.field1.data == 'xxx1'
        assert form.field2.data == 'xxx2'

        # validate and check again
        success = await form.validate()
        assert success == False
        assert form.field1.data == 'xxx1'
        assert form.field2.data == 'xxx2'

        # check errors
        assert len(form.errors['field1']) == 1
        assert form.errors['field1'][0] == 'Field value is incorrect.'

        assert len(form.errors['field2']) == 1
        assert form.errors['field2'][0] == 'Field value is incorrect.'
        
        return PlainTextResponse()

    client.post('/', data={'field1': 'xxx1', 'field2': 'xxx2'})


def test_data_required_error(app, client, FormWithAsyncValidators):
    @app.route('/', methods=['POST'])
    async def index(request):
        form = await FormWithAsyncValidators.from_formdata(request)
        assert form.field1.data == 'xxx1'
        assert form.field2.data == None

        # validate and check again
        success = await form.validate()
        assert success == False
        assert form.field1.data == 'xxx1'

        # check errors
        assert len(form.errors['field1']) == 1
        assert form.errors['field1'][0] == 'Field value is incorrect.'

        assert len(form.errors['field2']) == 1
        assert form.errors['field2'][0] == 'This field is required.'
        
        return PlainTextResponse()

    client.post('/', data={'field1': 'xxx1'})
