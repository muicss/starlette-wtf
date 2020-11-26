from starlette.responses import PlainTextResponse


def test_custom_validator_success(app, client, FormWithCustomValidators):
    @app.route('/', methods=['POST'])
    async def index(request):
        form = await FormWithCustomValidators.from_formdata(request)
        assert form.field1.data == 'value1'
        assert form.field2.data == 'value2'

        # validate and check again
        await form.validate()
        assert form.field1.data == 'value1'
        assert form.field2.data == 'value2'

        return PlainTextResponse()

    client.post('/', data={'field1': 'value1', 'field2': 'value2'})


def test_custom_validator_failure(app, client, FormWithCustomValidators):
    @app.route('/', methods=['POST'])
    async def index(request):
        form = await FormWithCustomValidators.from_formdata(request)
        await form.validate()
        assert 'field1' in form.errors
        assert 'field2' in form.errors
        return PlainTextResponse()

    client.post('/', data={'field1': 'xxx', 'field2': 'xxx'})


def test_custom_async_validator_success(app, client, FormWithCustomAsyncValidators):
    @app.route('/', methods=['POST'])
    async def index(request):
        form = await FormWithCustomAsyncValidators.from_formdata(request)
        assert form.field1.data == 'value1'
        assert form.field2.data == 'value2'

        # validate and check again
        await form.validate()
        assert form.field1.data == 'value1'
        assert form.field2.data == 'value2'

        return PlainTextResponse()

    client.post('/', data={'field1': 'value1', 'field2': 'value2'})
