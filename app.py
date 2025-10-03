import streamlit as st
import speedtest


def custom_metric(*, label: str, value: str) -> None:
    st.markdown(f"#### **{label}**")
    st.markdown(f"#### {value}")


def run_speed_test() -> dict[str, float]:
    config = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }

    st_instance = speedtest.Speedtest(config=config, secure=True)

    server_info_placeholder = st.empty()
    server_info_placeholder.info("Finding the best server...")

    best_server = st_instance.get_best_server()

    with server_info_placeholder.container():
        st.subheader("Best Server")

        col1, col2, col3 = st.columns(3, border=True)

        with col1:
            custom_metric(
                label=f":material/person: {st_instance.results.client['isp']}",
                value=f"{st_instance.results.client['ip']}",
            )

        with col2:
            custom_metric(
                label=":material/host: Host",
                value=f"{best_server['sponsor']}",
            )

        with col3:
            custom_metric(
                label=":material/location_on: Location",
                value=f"{best_server['name']}, {best_server['country']}",
            )

    with st.spinner("Testing download speed..."):
        download_speed = st_instance.download() / 1_000_000

    with st.spinner("Testing upload speed..."):
        upload_speed = st_instance.upload() / 1_000_000

    ping = st_instance.results.ping

    return {"download": download_speed, "upload": upload_speed, "ping": ping}


st.set_page_config(page_title="Internet Speed Test", page_icon="⚡", layout="wide")

st.title("⚡ Internet Speed Test")
st.write("Click the button below to start the test.")

if st.button("Run Speed Test"):
    try:
        results = run_speed_test()

        st.subheader("Test Results:")

        col1, col2, col3 = st.columns(3, border=True)

        with col1:
            custom_metric(
                label=":material/download: Download Speed",
                value=f"{results['download']:.2f} Mbps",
            )

        with col2:
            custom_metric(
                label=":material/upload: Upload Speed",
                value=f"{results['upload']:.2f} Mbps",
            )

        with col3:
            custom_metric(
                label=":material/signal_cellular_alt: Ping",
                value=f"{results['ping']:.2f} ms",
            )

    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.info("Please check your internet connection and try again.")
