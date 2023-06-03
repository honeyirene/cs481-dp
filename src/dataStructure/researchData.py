import pandas as pd
from models.graphDataModel import GraphPlotDataModel, GraphTraceDataModel


class ResearchDataFactory:
    def __init__(self):
        EMO_ANN_EXTERNAL = pd.read_csv(
            "./dataset/emotion_annotations/aggregated_external_annotations/P4.external.csv"
        )
        EMO_ANN_PARTNER = pd.read_csv(
            "./dataset/emotion_annotations/partner_annotations/P4.partner.csv"
        )
        EMO_ANN_SELF = pd.read_csv(
            "./dataset/emotion_annotations/self_annotations/P4.self.csv"
        )

        E4_ACC = pd.read_csv("./dataset/e4_data/4/E4_ACC.csv")
        E4_BVP = pd.read_csv("./dataset/e4_data/4/E4_BVP.csv")
        E4_EDA = pd.read_csv("./dataset/e4_data/4/E4_EDA.csv")
        E4_HR = pd.read_csv("./dataset/e4_data/4/E4_HR.csv")
        E4_IBI = pd.read_csv("./dataset/e4_data/4/E4_IBI.csv")
        E4_TEMP = pd.read_csv("./dataset/e4_data/4/E4_TEMP.csv")

        ATTENTION = pd.read_csv("./dataset/neurosky_polar_data/4/Attention.csv")
        BRAINWAVE = pd.read_csv("./dataset/neurosky_polar_data/4/BrainWave.csv")
        MEDITATION = pd.read_csv("./dataset/neurosky_polar_data/4/Meditation.csv")
        POLAR_HR = pd.read_csv("./dataset/neurosky_polar_data/4/Polar_HR.csv")

        traceData_acc_x = GraphTraceDataModel("timestamp", "x", "x axis")
        traceData_acc_y = GraphTraceDataModel("timestamp", "y", "y axis")
        traceData_acc_z = GraphTraceDataModel("timestamp", "z", "z axis")
        self.plotData_acc = GraphPlotDataModel(
            "g", E4_ACC, [traceData_acc_x, traceData_acc_y, traceData_acc_z]
        )

        traceData_bvp = GraphTraceDataModel("timestamp", "value", "BVP")
        self.plotData_bvp = GraphPlotDataModel("PPG", E4_BVP, [traceData_bvp])

        traceData_eda = GraphTraceDataModel("timestamp", "value", "EDA")
        self.plotData_eda = GraphPlotDataModel("uS", E4_EDA, [traceData_eda])

        HR_DF = E4_HR.copy()
        HR_DF["e4"] = E4_HR["value"]
        HR_DF["ecg"] = POLAR_HR["value"]
        traceData_hr_e4 = GraphTraceDataModel("timestamp", "e4", "E4")
        traceData_hr_ecg = GraphTraceDataModel("timestamp", "ecg", "ECG")
        self.plotData_hr = GraphPlotDataModel(
            "Heart Rate", HR_DF, [traceData_hr_e4, traceData_hr_ecg]
        )

        traceData_ibi = GraphTraceDataModel("timestamp", "value", "IBI")
        self.plotData_ibi = GraphPlotDataModel("IBI", E4_IBI, [traceData_ibi])

        traceData_temp = GraphTraceDataModel("timestamp", "value", "℃")
        self.plotData_temp = GraphPlotDataModel(
            "Temperature", E4_TEMP, [traceData_temp]
        )

        traceData_bw_high_alpha = GraphTraceDataModel(
            "timestamp", "highAlpha", "high-alpha"
        )
        traceData_bw_high_beta = GraphTraceDataModel(
            "timestamp", "highBeta", "high-beta"
        )
        traceData_bw_middle_gamma = GraphTraceDataModel(
            "timestamp", "middleGamma", "middle-gamma"
        )
        traceData_bw_low_alpha = GraphTraceDataModel(
            "timestamp", "lowAlpha", "low-alpha"
        )
        traceData_bw_low_beta = GraphTraceDataModel("timestamp", "lowBeta", "low-beta")
        traceData_bw_low_gamma = GraphTraceDataModel(
            "timestamp",
            "lowGamma",
            "low-gamma",
        )
        traceData_bw_delta = GraphTraceDataModel("timestamp", "delta", "delta")
        traceData_bw_theta = GraphTraceDataModel("timestamp", "theta", "theta")
        self.plotData_bw = GraphPlotDataModel(
            "relative power",
            BRAINWAVE,
            [
                traceData_bw_high_alpha,
                traceData_bw_high_beta,
                traceData_bw_middle_gamma,
                traceData_bw_low_alpha,
                traceData_bw_low_beta,
                traceData_bw_low_gamma,
                traceData_bw_delta,
                traceData_bw_theta,
            ],
        )

        ATME_DF = ATTENTION.copy()
        ATME_DF["at"] = ATTENTION["value"]
        ATME_DF["me"] = MEDITATION["value"]
        traceData_att = GraphTraceDataModel("timestamp", "at", "attention")
        traceData_med = GraphTraceDataModel("timestamp", "me", "meditation")
        self.plotData_etc = GraphPlotDataModel(
            "attention & meditation", ATME_DF, [traceData_att, traceData_med]
        )

        basetimestamp = self.plotData_acc.df["timestamp"][0]
        EMO_ANN_EXTERNAL["timestamp"] = (
            EMO_ANN_EXTERNAL["seconds"]
            .astype(int)
            .apply(lambda x: x * 1000 + basetimestamp)
        )
        EMO_ANN_PARTNER["timestamp"] = (
            EMO_ANN_PARTNER["seconds"]
            .astype(int)
            .apply(lambda x: x * 1000 + basetimestamp)
        )
        EMO_ANN_SELF["timestamp"] = (
            EMO_ANN_SELF["seconds"]
            .astype(int)
            .apply(lambda x: x * 1000 + basetimestamp)
        )

        traceData_ext_arousal = GraphTraceDataModel("timestamp", "arousal", "arousal")
        traceData_ext_valence = GraphTraceDataModel("timestamp", "valence", "valence")
        traceData_ext_cheerful = GraphTraceDataModel(
            "timestamp", "cheerful", "cheerful"
        )
        traceData_ext_happy = GraphTraceDataModel("timestamp", "happy", "happy")
        traceData_ext_angry = GraphTraceDataModel("timestamp", "angry", "angry")
        traceData_ext_nervous = GraphTraceDataModel("timestamp", "nervous", "nervous")
        traceData_ext_sad = GraphTraceDataModel("timestamp", "sad", "sad")
        traceData_ext_boredom = GraphTraceDataModel("timestamp", "boredom", "boredom")
        traceData_ext_confusion = GraphTraceDataModel(
            "timestamp", "confusion", "confusion"
        )
        traceData_ext_delight = GraphTraceDataModel("timestamp", "delight", "delight")
        traceData_ext_concentration = GraphTraceDataModel(
            "timestamp", "concentration", "concentration"
        )
        traceData_ext_frustration = GraphTraceDataModel(
            "timestamp", "frustration", "frustration"
        )
        traceData_ext_surprise = GraphTraceDataModel(
            "timestamp", "surprise", "surprise"
        )
        traceData_ext_none_1 = GraphTraceDataModel(
            "timestamp", "none_1", "commonly used BROMP none"
        )
        traceData_ext_confrustion = GraphTraceDataModel(
            "timestamp", "confrustion", "confrustion"
        )
        traceData_ext_contempt = GraphTraceDataModel(
            "timestamp", "contempt", "contempt"
        )
        traceData_ext_dejection = GraphTraceDataModel(
            "timestamp", "dejection", "dejection"
        )
        traceData_ext_disgust = GraphTraceDataModel("timestamp", "disgust", "disgust")
        traceData_ext_eureka = GraphTraceDataModel("timestamp", "eureka", "eureka")
        traceData_ext_pride = GraphTraceDataModel("timestamp", "pride", "pride")
        traceData_ext_sorrow = GraphTraceDataModel("timestamp", "sorrow", "sorrow")
        traceData_ext_none_2 = GraphTraceDataModel(
            "timestamp", "none_2", "less commonly used BROMP none"
        )

        self.plotData_emo_ann_ext = GraphPlotDataModel(
            "external emotion annotation",
            EMO_ANN_EXTERNAL,
            [
                traceData_ext_arousal,
                traceData_ext_valence,
                traceData_ext_cheerful,
                traceData_ext_happy,
                traceData_ext_angry,
                traceData_ext_nervous,
                traceData_ext_sad,
                traceData_ext_boredom,
                traceData_ext_confusion,
                traceData_ext_delight,
                traceData_ext_concentration,
                traceData_ext_frustration,
                traceData_ext_surprise,
                traceData_ext_none_1,
                traceData_ext_confrustion,
                traceData_ext_contempt,
                traceData_ext_dejection,
                traceData_ext_disgust,
                traceData_ext_eureka,
                traceData_ext_pride,
                traceData_ext_sorrow,
                traceData_ext_none_2,
            ],
        )

        traceData_pnr_arousal = GraphTraceDataModel("timestamp", "arousal", "arousal")
        traceData_pnr_valence = GraphTraceDataModel("timestamp", "valence", "valence")
        traceData_pnr_cheerful = GraphTraceDataModel(
            "timestamp", "cheerful", "cheerful"
        )
        traceData_pnr_happy = GraphTraceDataModel("timestamp", "happy", "happy")
        traceData_pnr_angry = GraphTraceDataModel("timestamp", "angry", "angry")
        traceData_pnr_nervous = GraphTraceDataModel("timestamp", "nervous", "nervous")
        traceData_pnr_sad = GraphTraceDataModel("timestamp", "sad", "sad")
        traceData_pnr_boredom = GraphTraceDataModel("timestamp", "boredom", "boredom")
        traceData_pnr_confusion = GraphTraceDataModel(
            "timestamp", "confusion", "confusion"
        )
        traceData_pnr_delight = GraphTraceDataModel("timestamp", "delight", "delight")
        traceData_pnr_concentration = GraphTraceDataModel(
            "timestamp", "concentration", "concentration"
        )
        traceData_pnr_frustration = GraphTraceDataModel(
            "timestamp", "frustration", "frustration"
        )
        traceData_pnr_surprise = GraphTraceDataModel(
            "timestamp", "surprise", "surprise"
        )
        traceData_pnr_none_1 = GraphTraceDataModel(
            "timestamp", "none_1", "commonly used BROMP none"
        )
        traceData_pnr_confrustion = GraphTraceDataModel(
            "timestamp", "confrustion", "confrustion"
        )
        traceData_pnr_contempt = GraphTraceDataModel(
            "timestamp", "contempt", "contempt"
        )
        traceData_pnr_dejection = GraphTraceDataModel(
            "timestamp", "dejection", "dejection"
        )
        traceData_pnr_disgust = GraphTraceDataModel("timestamp", "disgust", "disgust")
        traceData_pnr_eureka = GraphTraceDataModel("timestamp", "eureka", "eureka")
        traceData_pnr_pride = GraphTraceDataModel("timestamp", "pride", "pride")
        traceData_pnr_sorrow = GraphTraceDataModel("timestamp", "sorrow", "sorrow")
        traceData_pnr_none_2 = GraphTraceDataModel(
            "timestamp", "none_2", "less commonly used BROMP none"
        )

        self.plotData_emo_ann_pnr = GraphPlotDataModel(
            "partner emotion annotation",
            EMO_ANN_PARTNER,
            [
                traceData_pnr_arousal,
                traceData_pnr_valence,
                traceData_pnr_cheerful,
                traceData_pnr_happy,
                traceData_pnr_angry,
                traceData_pnr_nervous,
                traceData_pnr_sad,
                traceData_pnr_boredom,
                traceData_pnr_confusion,
                traceData_pnr_delight,
                traceData_pnr_concentration,
                traceData_pnr_frustration,
                traceData_pnr_surprise,
                traceData_pnr_none_1,
                traceData_pnr_confrustion,
                traceData_pnr_contempt,
                traceData_pnr_dejection,
                traceData_pnr_disgust,
                traceData_pnr_eureka,
                traceData_pnr_pride,
                traceData_pnr_sorrow,
                traceData_pnr_none_2,
            ],
        )

        traceData_self_arousal = GraphTraceDataModel("timestamp", "arousal", "arousal")
        traceData_self_valence = GraphTraceDataModel("timestamp", "valence", "valence")
        traceData_self_cheerful = GraphTraceDataModel(
            "timestamp", "cheerful", "cheerful"
        )
        traceData_self_happy = GraphTraceDataModel("timestamp", "happy", "happy")
        traceData_self_angry = GraphTraceDataModel("timestamp", "angry", "angry")
        traceData_self_nervous = GraphTraceDataModel("timestamp", "nervous", "nervous")
        traceData_self_sad = GraphTraceDataModel("timestamp", "sad", "sad")
        traceData_self_boredom = GraphTraceDataModel("timestamp", "boredom", "boredom")
        traceData_self_confusion = GraphTraceDataModel(
            "timestamp", "confusion", "confusion"
        )
        traceData_self_delight = GraphTraceDataModel("timestamp", "delight", "delight")
        traceData_self_concentration = GraphTraceDataModel(
            "timestamp", "concentration", "concentration"
        )
        traceData_self_frustration = GraphTraceDataModel(
            "timestamp", "frustration", "frustration"
        )
        traceData_self_surprise = GraphTraceDataModel(
            "timestamp", "surprise", "surprise"
        )
        traceData_self_none_1 = GraphTraceDataModel(
            "timestamp", "none_1", "commonly used BROMP none"
        )
        traceData_self_confrustion = GraphTraceDataModel(
            "timestamp", "confrustion", "confrustion"
        )
        traceData_self_contempt = GraphTraceDataModel(
            "timestamp", "contempt", "contempt"
        )
        traceData_self_dejection = GraphTraceDataModel(
            "timestamp", "dejection", "dejection"
        )
        traceData_self_disgust = GraphTraceDataModel("timestamp", "disgust", "disgust")
        traceData_self_eureka = GraphTraceDataModel("timestamp", "eureka", "eureka")
        traceData_self_pride = GraphTraceDataModel("timestamp", "pride", "pride")
        traceData_self_sorrow = GraphTraceDataModel("timestamp", "sorrow", "sorrow")
        traceData_self_none_2 = GraphTraceDataModel(
            "timestamp", "none_2", "less commonly used BROMP none"
        )

        self.plotData_emo_ann_self = GraphPlotDataModel(
            "self emotion annotation",
            EMO_ANN_SELF,
            [
                traceData_self_arousal,
                traceData_self_valence,
                traceData_self_cheerful,
                traceData_self_happy,
                traceData_self_angry,
                traceData_self_nervous,
                traceData_self_sad,
                traceData_self_boredom,
                traceData_self_confusion,
                traceData_self_delight,
                traceData_self_concentration,
                traceData_self_frustration,
                traceData_self_surprise,
                traceData_self_none_1,
                traceData_self_confrustion,
                traceData_self_contempt,
                traceData_self_dejection,
                traceData_self_disgust,
                traceData_self_eureka,
                traceData_self_pride,
                traceData_self_sorrow,
                traceData_self_none_2,
            ],
        )


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    # view.run_server(debug=True)
    print("skip")
