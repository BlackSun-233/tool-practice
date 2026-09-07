FROM python:3.12‑slim
COPY dist /dist
RUN pip install /dist/demo_pkg_blacksun‑0.0.1‑*.whl
CMD ["python","‑c","from demo_pkg_blacksun import hello;hello()"]
