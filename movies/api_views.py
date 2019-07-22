from django.db.models import Max, Q
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


# Create your views here.

# 영화 전체 목록 리스트
class MovieList(generics.ListAPIView):
    """
        전체 영화 목록입니다

        ---
            - id : 영화의 고유 ID
            - name : 영화의 이름
            - horizontal_image_path : 영화 가로 이미지 경로
            - vetical_image : 영화 세로 이미지(추후 변경예정)


    """

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class HomePage(generics.ListAPIView):
    """
        맨처음 홈페이지 화면입니다

        ---
            - 맨처음 나오는 영화는 맨위에 크게 들어갈 영화 입니다.

            헤더에
            - Authorization : Token 토큰 값
            - subuserid : 프로필계정의 ID

            를 입력해 주세요 (subuserid는 언더바(_)가 없습니다)
    """

    serializer_class = HomePageSerializer

    def get_queryset(self):
        # 랜덤하게 영화 1개를 가져오기 위함
        max_id = Movie.objects.all().aggregate(max_id=Max('id'))['max_id']
        while True:
            pk = random.randint(1, max_id)

            # 랜덤으로 선택한 영화 1편
            queryset = Movie.objects.filter(pk=pk)
            if queryset:
                break

        return queryset

    def get_serializer_context(self):
        sub_user_id = self.request.META['HTTP_SUBUSERID']
        context = super().get_serializer_context()
        context['sub_user_id'] = sub_user_id
        return context


# 영화 탭을 누르면 나오는 화면에 필요한 영화들의 목록
class GenreSelectBefore(generics.ListAPIView):
    """

        영화 탭을 누르면 나오는 화면에 데이터를 전달하는 뷰 입니다

       ---

            헤더에
            - Authorization : Token 토큰 값
            - subuserid : 프로필계정의 ID

            를 입력해 주세요 (subuserid는 언더바(_)가 없습니다)


           맨 처음 나오는 영화 1개는 맨위에 크게 등록되는 영화 입니다

            - id : 영화의 id
            - name : 영화의 이름
            - horizontal_image_path : 가로 이미지의 path
            - vertical_image : 세로 이미지 파일

    """
    serializer_class = GenreSelectBeforeSerializer

    def get_queryset(self):
        # 랜덤하게 영화 1개를 가져오기 위함
        max_id = Movie.objects.all().aggregate(max_id=Max('id'))['max_id']
        while True:
            pk = random.randint(1, max_id)

            # 랜덤으로 선택한 영화 1편
            queryset = Movie.objects.filter(pk=pk)
            if queryset:
                break

        return queryset

    def get_serializer_context(self):
        sub_user_id = self.request.META['HTTP_SUBUSERID']
        print(sub_user_id)
        genre_list = ['한국 영화', '외국 영화', '어린이', '가족', '액션', '스릴러', 'SF',
                      '판타지', '범죄', '호러', '다큐멘터리', '로맨스', '코미디', '애니', '오리지널']
        context = super().get_serializer_context()
        context['genre_list'] = genre_list
        context['sub_user_id'] = sub_user_id
        return context


# 앱을 위한 뷰
class PreviewCellList(generics.ListAPIView):
    """
        앱을 위한 프리뷰셀 API입니다

        ---

        ```
            GET 으로 요청 하시면 됩니다

            리턴값 :
            - id : 영화의 고유 ID
            - name : 영화 이름
            - circle_image : 영화의 원형 이미지
            - logo_image_path : 영화의 로고 이미지 path
            - video_file : 영화 파일
            - vertical_sample_video_file : 영화의 세로 샘플 영상
        ```
    """

    serializer_class = PreviewCellListSerializer

    def get_queryset(self):
        queryset = Movie.objects.all().order_by('?')[:10]

        return queryset


# 영화 등록
# class MovieCerate(generics.CreateAPIView):
#     """
#         영화 등록 API 입니다
#
#         ---
#             - name : 영화 이름
#             - production_date : 영화 개봉 날짜
#             - uploaded_date : 영화 등록(업로드) 날짜
#             - synopsis : 영화 줄거리
#             - running_time : 영화 러닝타임
#             - view_count : 영화 조회수
#             - logo_image_path : 영화 로고 이미지 경로
#             - horizontal_image_path : 영화 가로 이미지 경로
#             - degree : 영화 등급 (Ex.청소년 관람불가, 15세 등등)
#             - directors : 영화 감독
#             - actors : 배우
#             - feature : 영화 특징(Ex.흥미진진)
#             - author : 각본가
#             - genre : 장르
#
#     """
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


# 영화 장르 리스트
class GenreList(generics.ListAPIView):
    """
        영화 장르 리스트입니다

        ---

            헤더에

            - Authorization : Token 토큰 값

            를 입력해 주세요


            - id : 영화 장르 ID
            - name : 영화 장르
    
    """

    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer


# 장르별 영화 리스트를 전체로 뿌려주기
# class ListByMovieGenre(generics.ListAPIView):
#     """
#         장르별 영화 리스트 입니다
#
#
#         ---
#
#             - 요청할때 movie/genre/'카테고리 명'/list/로 요청하시면 됩니다
#                 - Ex) movie/genre/액션/list/
#                 - Ex) movie/genre/스릴러/list/
#
#                 - name : 영화 이름
#                 - video_file : 비디오파일
#                 - sample_video_file : 샘플 비디오 파일
#                 - production_date : 영화 개봉 날짜
#                 - uploaded_date : 영화 등록(업로드) 날짜
#                 - synopsis : 영화 줄거리
#                 - running_time : 영화 러닝타임
#                 - view_count : 영화 조회수
#                 - logo_image_path : 로고 이미지의 경로
#                 - horizontal_image_path : 가로 이미지 경로
#                 - vertical_image : 세로 이미지(차후 변경 예정)
#                 - circle_image : 원형 이미지(차후 변경예정)
#                 - degree : 영화 등급 (Ex.청소년 관람불가, 15세 등등)
#                 - directors : 영화 감독
#                 - actors : 배우
#                 - feature : 영화 특징(Ex.흥미진진)
#                 - author : 각본가
#                 - genre : 장르
#
#     """
#
#     # queryset = Movie.objects.all()
#     serializer_class = ListByMovieGenreSerializer
#
#     def get_queryset(self):
#         if 'kind' in self.kwargs:
#             kind = self.kwargs['kind']
#         else:
#             kind = None
#
#         queryset = Movie.objects.filter(genre__name__icontains=kind).distinct()[:20]
#
#         return queryset


# 해당 유저의 찜 영화 목록
# 유저별 찜목록 영화 리스트
class MarkedList(generics.ListAPIView):
    """
        유저별 찜 목록 영화 리스트 입니다

        ---

            헤더에
            - Authorization : Token 토큰 값
            - subuserid : 프로필계정의 ID

            를 입력해 주세요 (subuserid는 언더바(_)가 없습니다)


            - 요청할때 "/movies/my_list" 로 요청하시면 됩니다

                - Ex) /movies/my_list/

                - id : 영화의 고유 ID 값
                - name : 영화 이름
                - horizontal_image_path : 가로 이미지 경로
                - vertical_image : 세로 이미지(차후 변경 예정)

    """

    serializer_class = MarkedListSerializer

    def get_queryset(self):
        sub_user_id = self.request.META['HTTP_SUBUSERID']
        queryset = Movie.objects.filter(like__sub_user=sub_user_id, like__marked=True)
        return queryset


# 영화 상세정보 뷰
class MovieDetail(generics.RetrieveAPIView):
    """
        영화 디테일 페이지 url 입니다.

        ---

            헤더에

            - Authorization : Token 토큰 값
            - subuserid : 프로필계정의 ID

            를 입력해 주세요 (subuserid는 언더바(_)가 없습니다)




            - 요청할때 "/movie/'영화 ID값'" 으로 요청하시면 됩니다.

                - Ex) /movie/2
                - Ex) /movie/7

                - id : 영화의 고유 ID 값
                - name : 영화 이름
                - video_file : 비디오파일
                - sample_video_file : 샘플 비디오 파일
                - production_date : 영화 개봉 날짜
                - uploaded_date : 영화 등록(업로드) 날짜
                - synopsis : 영화 줄거리
                - running_time : 영화 러닝타임
                - view_count : 영화 조회수
                - logo_image_path : 로고 이미지의 경로
                - horizontal_image_path : 가로 이미지 경로
                - vertical_image : 세로 이미지(차후 변경 예정)
                - circle_image : 원형 이미지(차후 변경예정)
                - degree : 영화 등급 (Ex.청소년 관람불가, 15세 등등)
                - directors : 영화 감독
                - actors : 배우
                - feature : 영화 특징(Ex.흥미진진)
                - author : 각본가
                - genre : 장르
                - marked : 유저가 찜한 영화인
                - like : 유저가 좋아요한 영화인지, 싫어요한 영화인지 (평가안함 = 0 , 좋아요 = 1, 싫어요 = 2)
                - total_minute : 시간을 분으로 환산한 값
                - match_rate : 일치율(현재 70~97 랜덤, 추후 업데이트 예정)
                - to_be_continue : 유저가 재생을 멈춘시간
                - remaining_time : running_time - to_be_continue
                - can_i_store : 저장가능 여부


    """
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        sub_user_id = self.request.META['HTTP_SUBUSERID']
        context['sub_user_id'] = sub_user_id
        return context


# 시청중인 목록 뷰
class FollowUpMovies(generics.ListAPIView):
    """
        메인화면에서 보여줄 시청 중인 영화리스트 url 입니다.

        ---
            - 요청할때 /movie/followup/'sub_user_id 값' 으로 요청하시면 됩니다.

                - Ex) /movie/followup/1
                - Ex) /movie/followup/25

                - id : 영화의 고유 ID 값
                - name : 영화 이름
                - video_file : 비디오파일
                - logo_image_path : 로고 이미지의 경로
                - horizontal_image_path : 가로 이미지 경로
                - vertical_image : 세로 이미지(차후 변경 예정)
                - to_be_continue : 유저가 재생을 멈춘시간
    """

    # queryset = Movie.objects.all()
    serializer_class = MovieContinueSerializer

    def get_queryset(self):
        sub_user_id = self.request.META['HTTP_SUBUSERID']
        queryset = MovieContinue.objects.filter(sub_user_id=sub_user_id)
        return queryset


# 장르별 영화 리스트
class MovieListByGenre(APIView):
    """
        SADFSDFDFSDFSDFD

        ---
            ASFSDFDSFFDS

    """

    ## 서브유저 정보 헤더에서 받아오기

    def get(self, request, format=None, **kwargs):
        vertical_genre = self.kwargs['genre_key']

        genre_list = [
            '한국',
            '미국',
            '어린이',
            '액션',
            '스릴러',
            'sf',
            '판타지',
            '범죄',
            '호러',
            '다큐',
            '로맨스',
            '코미디',
            '애니',
            '외국',
        ]

        context = {}
        vertical_q = Q(genre__name__icontains=vertical_genre)

        for genre in genre_list:
            if vertical_genre == genre:
                continue
            else:
                horizontal_q = Q(genre__name__icontains=genre)
                if vertical_genre == '외국':
                    queryset = Movie.objects.exclude(genre__name__icontains='한국').filter(horizontal_q)

                else:
                    if genre == '외국':
                        queryset = Movie.objects.exclude(genre__name__icontains='한국').filter(vertical_q)
                    else:
                        queryset = Movie.objects.filter(vertical_q).filter(horizontal_q)

                if queryset.count() < 3:
                    continue
                serializer = MovieListByGenreSerializer(queryset.distinct()[:20], many=True)
                context[f'{genre}'] = serializer.data
        if vertical_genre == '외국':
            vertical_queryset = Movie.objects.exclude(genre__name__icontains='한국')
        else:
            vertical_queryset = Movie.objects.filter(vertical_q)

        vertical_serializer = MovieListByGenreSerializer(vertical_queryset.distinct(), many=True)
        context[f'{vertical_genre}'] = vertical_serializer.data

        return Response(context)