FROM python
WORKDIR /files/
COPY . /files/
# CMD [ "python", "test/test_main_module.py" ]
CMD ["python", "-m", "unittest", "test.test_main_module"]
